// lo vamos a manejar por evnetos 

document.addEventListener('DOMContentLoaded' , function(){
    // tomamos el ide del boton 
    var boton = document.getElementById('boton')

    boton.addEventListener('click' ,function(){
        // mandmos a llamar ala funcion de valuidacion 
        validaciones()
    })
})

function validaciones(){
    // primer validacion de campo vacio 

    var campo_numerico = document.getElementById('amount').value 
    var mensaje = document.getElementById('span1')
    var imagen = document.getElementById('imagen')
    imagen.src = "compu.gif"
    mensaje.innerText = " "

    if(campo_numerico == ""){

        mensaje.innerText = "No ingresaste nada"
        imagen.src = "error.GIF"

    }else {
       var bandera = isNaN(campo_numerico)

       if(bandera == true){
        mensaje.innerText = "Es una Cadena"
        imagen.src = "error.GIF"
       }else{
        // ahora podemos trabajar ocn numeros 
        var numero = parseFloat(campo_numerico)
        if (numero <= 0 ){
            mensaje.innerText = "Numero invalido"
            imagen.src = "error.GIF"
        }else {
            // creo que son todas las validaciones o lo limito a 100 es que no se jajajaj 
            convertirDivisa() // ahora si hacemos lo de la api 

        }
       }

    }
}
function convertirDivisa() {
    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    const apiKey = 'TU_CLAVE_API'; 
    const apiUrl = `https://open.er-api.com/v6/latest/${fromCurrency}?apikey=${apiKey}`;

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error de red - ${response.status}: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        const exchangeRate = data.rates[toCurrency];
        const resultado = amount * exchangeRate;

        document.getElementById('resultado').textContent = `${amount} ${fromCurrency} es aproximadamente ${resultado.toFixed(2)} ${toCurrency}`;
      })
      .catch(error => {
        console.error('Error al recuperar datos:', error);
      });
  }
