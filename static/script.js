// Validação no navegador (JavaScript) antes de enviar ao Python.
const form = document.getElementById("form-calc");
const aviso = document.getElementById("aviso");

function paraNumero(texto) {
  return Number(texto.trim().replace(",", "."));
}

if (form) {
  form.addEventListener("submit", (e) => {
    const a = paraNumero(form.a.value);
    const b = paraNumero(form.b.value);

    if (form.a.value.trim() === "" || form.b.value.trim() === "" || isNaN(a) || isNaN(b)) {
      e.preventDefault();
      aviso.textContent = "Digite dois números válidos.";
      return;
    }
    if (OPERACAO === "divisao" && b === 0) {
      e.preventDefault();
      aviso.textContent = "Não é possível dividir por zero.";
      return;
    }
    aviso.textContent = "";
  });
}
