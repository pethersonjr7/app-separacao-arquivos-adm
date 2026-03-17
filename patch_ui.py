import sys

def patch_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    old_code = """
            try:
                const response = await fetch('/process', {
                    method: 'POST',
                    body: formData
                });
"""

    new_code = """
            // Add interval to update logs with a "Still writing..." message if it takes too long
            addLog("Enviando arquivo e aguardando processamento. Isso pode levar alguns minutos em arquivos grandes...");
            
            try:
                const response = await fetch('/process', {
                    method: 'POST',
                    body: formData
                });
"""
    
    # We also update the html message itself
    old_html = """
                    <button type="submit" class="btn-primary" id="processBtn">
                        <span class="btn-text">Processar Tudo</span>
                        <div class="loader" id="loader"></div>
                    </button>
"""

    new_html = """
                    <button type="submit" class="btn-primary" id="processBtn">
                        <span class="btn-text">Processar Tudo</span>
                        <div class="loader" id="loader"></div>
                    </button>
                    <p id="longWaitMsg" style="display: none; font-size: 0.75rem; color: #f59e0b; margin-top: 8px; text-align: center;">O processamento de arquivos grandes pode levar até 15 minutos.</p>
"""

    old_js2 = """
            // UI Feedback
            processBtn.disabled = true;
            loader.style.display = 'block';
            btnText.textContent = 'Processando...';

            // Clean view for new process
            logsSection.style.display = 'block';
            logsContent.innerHTML = '';
            resultsContainer.style.display = 'none';
            welcomeMsg.style.display = 'none';
            addLog('Iniciando envio seguro...');
"""

    new_js2 = """
            // UI Feedback
            processBtn.disabled = true;
            loader.style.display = 'block';
            btnText.textContent = 'Processando...';
            document.getElementById('longWaitMsg').style.display = 'block';

            // Clean view for new process
            logsSection.style.display = 'block';
            logsContent.innerHTML = '';
            resultsContainer.style.display = 'none';
            welcomeMsg.style.display = 'none';
            addLog('Iniciando envio seguro...');
"""

    old_js3 = """
            } finally {
                processBtn.disabled = false;
                loader.style.display = 'none';
                btnText.textContent = 'Processar Tudo';
            }
"""

    new_js3 = """
            } finally {
                processBtn.disabled = false;
                loader.style.display = 'none';
                btnText.textContent = 'Processar Tudo';
                document.getElementById('longWaitMsg').style.display = 'none';
            }
"""

    if old_code in content and old_html in content:
        content = content.replace(old_code, new_code)
        content = content.replace(old_html, new_html)
        content = content.replace(old_js2, new_js2)
        content = content.replace(old_js3, new_js3)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Patched templates/index.html successfully")
    else:
        print("Could not find blocks to patch in index.html")

if __name__ == '__main__':
    patch_file('templates/index.html')
