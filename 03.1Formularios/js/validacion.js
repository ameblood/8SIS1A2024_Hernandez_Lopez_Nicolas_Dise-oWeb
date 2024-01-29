/**
 * es un lenguaje interpretado para lo cual denemos entender que el manejo de variables es no tipado 
 * js maneja var para cadenas, enteros, dobles, flotante etc
 * 
 * js es un lenguaje bajo multiparadigma 
 */
function validar(formulario){
    if(formulario.nombre.values.leng < 3 ){
        alert("escriba por lo menos mas de tres caracteres en el campo nombre");
        formulario.nombre.focus();
        
    }

    var checkOK = "qwertyuioplkjhgfdsazxcvbnm" + "QWERTYUIOPLKÑJHGFDSAZXCVBNM";

    var checkString = formulario.nombre.values;
    alert(checkString);
    var todoesvalido = tue;


    for(i=0;i<checkString.length; i++){
        var ch= checkString.charAT(i);
        for(j=0;j<checkOK.length;j++){
            if(ch==checkOK.charAt(j)){
                break;
            }
        }
        if(!todoesvalido){
            alert("favor de escribir solo letras en el campo de nombre");
            formulario.nombre.focus();
            return false;
        }
    }

}