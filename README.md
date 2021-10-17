# TechTestSorryRobots
This is a short repository to store the developed files for the test imposed.

Los pasos 1 al 6 los realiza sin ningún problema. Con respecto a la validación de la estructura, dentro de la función main verificamos que los keys sean de tipo `string`. Con esto validamos que las muestras tengan sus etiquetas en texto. Por otro lado, se realizó la clase `User` para darle la propiedad a cada item que pasa sobre esa lista. Allí verificamos que los items no sean `None`. De lo contrario, no realiza el proceso y el main imprime el raw.

Realicé un pequeño TDD, este está almacenado en el `test.py`, aunque solo pude verificar tres pequeños procesos sobre el dataset. Por último, con respecto a la escalabilidad el algoritmo puede analizar muchos items con elementos que pueden tener keys y values desconocidos, estos los imprime en raw al final. Ya para terminar, de querer añadir más instancias se puede hacer dentro del class `User`.

Agradezco la atención prestada.
