// Exibe uma mensagem no console para verificar o carregamento
console.log("Script carregado!");

// Você pode adicionar funcionalidade futura, como validação
document.querySelector("form").addEventListener("submit", function (e) {
    const urlInput = document.querySelector('input[type="url"]');
    if (!urlInput.value.startsWith("https://")) {
        e.preventDefault();
        alert("Por favor, insira um URL válido do YouTube!");
    }
});
