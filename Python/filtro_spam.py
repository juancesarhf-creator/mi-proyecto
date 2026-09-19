#Vector de correo eléctronico
correo = ["oferta", "gratis", "dinero", "ganar", "clic"]

#Vector de palabras comunes en correos de spam
spam_words = ["oferta", "gratis", "dinero", "ganar", "clic"]

#Calcular la cantidad de palabras spam en el correo
cantidad_spam = sum([1 for word in correo if word in spam_words])

if cantidad_spam > 2:
    print("¡Alerta! Este correo electrónico podría ser spam")
else:
    print("Este correo electrónico parece ser legítimo")
