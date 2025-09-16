# Зависимости от выбранной точности
Расчеты представлены в [descent.ipynb](descent.ipynb).
Метод AdaDelta реализован по [Matthew D. Zeiler. ADADELTA: An Adaptive Learning Rate Method. 2012](https://arxiv.org/abs/1212.5701)

## Критерий останова

$$\begin{equation}
    \Vert\nabla f(x_k)\Vert < \varepsilon.
\end{equation}$$

## Координаты минимума функции
<img src='readme_img/descent_img/x1_optim_Well-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/x2_optim_Well-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/x1_optim_Poorly-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/x2_optim_Poorly-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/x1_optim_Rosenbrock.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/x2_optim_Rosenbrock.png' style='width:100%; height:auto;'>

## Количество итераций
<img src='readme_img/descent_img/iter_count_Well-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/iter_count_Poorly-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/iter_count_Rosenbrock.png' style='width:100%; height:auto;'>

## Количество вычислений градиента
<img src='readme_img/descent_img/grad_count_Well-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/grad_count_Poorly-conditioned.png' style='width:100%; height:auto;'>
<img src='readme_img/descent_img/grad_count_Rosenbrock.png' style='width:100%; height:auto;'>

## Приложение с таблицами
