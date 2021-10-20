% importar datos 
% datos binarios transformados en escalas de grises:
img_grey = readNPY("C:\Users\marlo\OneDrive - Pontificia Universidad Javeriana\Maestria_IA\2130 Sistemas Inteligentes\Proyecto\Dataset\Imagenes_gris_240.npy");
img_grey = double(img_grey);

% Importar las etiquetas
etiquetas = readNPY("C:\Users\marlo\OneDrive - Pontificia Universidad Javeriana\Maestria_IA\2130 Sistemas Inteligentes\Proyecto\Dataset\labels.npy");
etiquetas = double(etiquetas);

%Vamos a utilizar la funcion 'fitrnet' utilizada en los ejemplos de Matlab. Ahora vamos a partir los datos en sets para entrenar y para hacer test.
rng("default") % Este es para establecer la semilla para reproducibilidad.
c = cvpartition(length(etiquetas), "HoldOut", 0.20); % separar el 20% para pruebas, se crean los indices
trainingIdx = training(c); % Indices por el conjunto de entrenamiento
XTrain = img_grey(trainingIdx,:); % subset de acuerdo a los indices de entrenamiento 
YTrain = etiquetas(trainingIdx);
testIdx = test(c); % indices para el conjunto de datos de prueba
XTest = img_grey(testIdx,:);
YTest = etiquetas(testIdx);

% entrenar Va a tener las siguiente especificaciones: va a tener 30 salidas en la primera capa y 10 salidas en las segunda. 
% Por defecto ambas capas van a usar un ReLU (Rectified Linear Unit) como funcion de activación. 
modelo = fitrnet(XTrain,YTrain, "Standardize", true, "LayerSizes", [30 10])

% una vez el modelo está entrenado, vamos a consultar los pesos y 'Biases', 
% los primeros dos elementos corresponden a los valores de las capas totalmente conectadas.  
modelo.LayerWeights{1}

% La capa final tiene una sola salida. El numero de capas corresponden a la primera dimension de la capa de pesos y Biases. 
size(modelo.LayerWeights{end})

%Ahora vamos a calcular el desempeño del modelo entrenado. Calculamos el error cuadrado medio (Mean Squared Error MSE) de los datos de prueba.
%Un error pequeño indica mejor performance:
testMSE = loss(modelo, XTest, YTest)

% Comparar los valores de prueba contra los valores reales en una grafica. Vertical los datos pronosticas y en el horizontal los datos reales.
testPredictions = predict(modelo, XTest);
plot(YTest, testPredictions, ".");
hold on
plot(YTest, YTest)
hold off
xlabel("Valor Real")
ylabel("valor Pronosticado")
