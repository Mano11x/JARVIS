(() => {
    const endpoint = '/assistant/api/chat/';
    const transcript = document.getElementById('transcript');
    const chatInput = document.getElementById('chat-input');
    const micBtn = document.getElementById('mic-btn');
    const settingsBtn = document.getElementById('settings-btn');
    const settingsModal = document.getElementById('settings-modal');
    const closeSettingsBtn = document.getElementById('close-settings');
    const helpModal = document.getElementById('help-modal');
    const closeHelpBtn = document.getElementById('close-help');
    const ollamaStatus = document.getElementById('ollama-status');

    // Footer Hotkeys
    const f1Help = document.querySelector('span[class*="cursor-pointer"]:nth-child(1)');
    const f2Logs = document.querySelector('span[class*="cursor-pointer"]:nth-child(2)');
    const escExit = document.querySelector('span[class*="cursor-pointer"]:nth-child(3)');

    const rightSidebar = document.querySelector('aside.fixed.right-6');

    function getCsrfToken() {
        return document.cookie.split('; ').reduce((token, cookie) => {
            const [name, value] = cookie.split('=');
            return name === 'csrftoken' ? decodeURIComponent(value) : token;
        }, '');
    }

    function appendMessage(sender, text, isError = false) {
        const line = document.createElement('div');
        line.className = 'py-1 transition-all duration-300';
        
        const prefix = document.createElement('span');
        prefix.className = sender === 'USER' ? 'text-primary/70 mr-2' : 'text-primary font-bold mr-2';
        prefix.textContent = `> ${sender}:`;

        const content = document.createElement('span');
        content.className = isError ? 'text-red-400' : 'text-white/90';
        content.textContent = text;

        line.appendChild(prefix);
        line.appendChild(content);
        transcript.appendChild(line);
        transcript.scrollTop = transcript.scrollHeight;
    }

    async function sendCommand() {
        const text = chatInput.value.trim();
        if (!text) return;

        appendMessage('USER', text);
        chatInput.value = '';

        // Temporary processing indicator
        const processLine = document.createElement('div');
        processLine.className = 'py-1 text-primary animate-pulse';
        processLine.textContent = '> JARVIS: PROCESSING REQUEST...';
        transcript.appendChild(processLine);
        transcript.scrollTop = transcript.scrollHeight;

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                body: JSON.stringify({ prompt: text }),
            });

            processLine.remove();

            if (!response.ok) {
                appendMessage('JARVIS', 'CONNECTION FAILURE TO STRATEGIC ENGINE.', true);
                return;
            }

            const data = await response.json();
            appendMessage('JARVIS', data.reply);
        } catch (error) {
            processLine.remove();
            appendMessage('JARVIS', 'CRITICAL INTERCONNECT ERROR DETECTED.', true);
        }
    }

    // Voice dictation using browser Web Speech API
    let recognition;
    function initSpeech() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
            console.warn("Web Speech API not supported in this browser.");
            return;
        }

        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onstart = () => {
            micBtn.style.borderColor = '#ef4444';
            micBtn.style.boxShadow = '0 0 25px rgba(239, 68, 68, 0.6)';
            chatInput.placeholder = 'LISTENING...';
        };

        recognition.onend = () => {
            micBtn.style.borderColor = '';
            micBtn.style.boxShadow = '';
            chatInput.placeholder = 'JARVIS, INITIALIZE DEFENSE PROTOCOL...';
        };

        recognition.onerror = (e) => {
            console.error("Speech recognition error:", e);
        };

        recognition.onresult = (event) => {
            const transcriptText = event.results[0][0].transcript;
            chatInput.value = transcriptText;
            sendCommand();
        };
    }

    function toggleMic() {
        if (!recognition) {
            appendMessage('JARVIS', 'SPEECH HANDSHAKE INCOMPATIBLE WITH THIS BROWSER.', true);
            return;
        }
        try {
            recognition.start();
        } catch (e) {
            recognition.stop();
        }
    }

    // Check if local Ollama is active
    async function checkOllama() {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                body: JSON.stringify({ prompt: 'how' }), // query to check if endpoint returns without 500
            });
            ollamaStatus.textContent = 'ONLINE';
            ollamaStatus.className = 'text-xs font-mono text-emerald-400';
        } catch {
            ollamaStatus.textContent = 'OFFLINE';
            ollamaStatus.className = 'text-xs font-mono text-red-500';
        }
    }

    function initialize() {
        initSpeech();
        appendMessage('JARVIS', 'NEURAL BUFFER RESTORED. STANDBY FOR INPUT.');
        checkOllama();

        // Submit message on Enter
        chatInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendCommand();
            }
        });

        // Modals Toggle
        settingsBtn.addEventListener('click', () => {
            settingsModal.classList.toggle('hidden');
            checkOllama();
        });
        closeSettingsBtn.addEventListener('click', () => settingsModal.classList.add('hidden'));

        // Help Modal Toggle
        const toggleHelp = () => helpModal.classList.toggle('hidden');
        f1Help.addEventListener('click', toggleHelp);
        closeHelpBtn.addEventListener('click', () => helpModal.classList.add('hidden'));

        // Toggle Logs Sidebar
        const toggleLogs = () => {
            if (rightSidebar) rightSidebar.classList.toggle('hidden');
        };
        f2Logs.addEventListener('click', toggleLogs);

        // Clear Conversation (Exit)
        const clearChat = () => {
            transcript.innerHTML = '';
            appendMessage('JARVIS', 'CONVERSATION HISTORY PURGED.');
        };
        escExit.addEventListener('click', clearChat);

        // Mic Click
        micBtn.addEventListener('click', toggleMic);

        // Keyboard Event Listeners for F1, F2, ESC
        window.addEventListener('keydown', (e) => {
            if (e.key === 'F1') {
                e.preventDefault();
                toggleHelp();
            } else if (e.key === 'F2') {
                e.preventDefault();
                toggleLogs();
            } else if (e.key === 'Escape') {
                e.preventDefault();
                clearChat();
                settingsModal.classList.add('hidden');
                helpModal.classList.add('hidden');
            }
        });
    }

    document.addEventListener('DOMContentLoaded', initialize);
})();
