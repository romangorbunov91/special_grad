# Траектории методов на графике линий уровня
Расчеты представлены в [plots.ipynb](plots.ipynb).

## Критерий останова

$$\begin{equation}
    \Vert\nabla f(x_k)\Vert < 1e-5.
\end{equation}$$

## Функция Розенброка
<img src='readme_img/func_img/trajectory_plots_Rosenbrock.png' style='width:100%; height:auto;'>

## Хорошо обусловленная (µ ≃ 1) двумерная квадратичная функция
<img src='readme_img/func_img/trajectory_plots_Well-conditioned.png' style='width:100%; height:auto;'>


## Плохо обусловленная (µ > 10) двумерная квадратичная функция
<img src='readme_img/func_img/trajectory_plots_Poorly-conditioned.png' style='width:100%; height:auto;'>