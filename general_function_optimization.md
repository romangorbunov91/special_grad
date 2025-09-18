# Исследование зависимости от заданной размерности и числа обусловленности квадратичных функций
Расчеты представлены в [general_function_optimization.ipynb](general_function_optimization.ipynb).

## Критерий останова

$$\begin{equation}
    \Vert\nabla f(x_k)\Vert < 1e-5.
\end{equation}$$

## Траектории
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_1.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_3.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_5.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_7.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_9.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_11.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_13.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_15.png' style='width:100%; height:auto;
'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_17.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/trajectory_plots_condition_number_19.png' style='width:100%; height:auto;'>

## Количество итераций
<img src='readme_img/general_function_optimization_img/iter_count_order_2.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_3.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_4.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_5.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_6.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_7.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_8.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_9.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_10.png' style='width:100%; height:auto;'>
<img src='readme_img/general_function_optimization_img/iter_count_order_11.png' style='width:100%; height:auto;'>

## Приложение с таблицами





<!-- START_ADAM --> 
### adam: Количество итераций ($\epsilon$=1e-05)
|   µ |   order=2 |   order=3 |   order=4 |   order=5 |   order=6 |   order=7 |   order=8 |   order=9 |   order=10 |   order=11 |
|----:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|-----------:|
|   1 |       584 |      2475 |       832 |      1695 |      5028 |      4533 |      2768 |      2323 |       4497 |       5075 |
|   3 |      1006 |      1617 |      1126 |      1058 |      2460 |      2643 |      1173 |      2477 |       1792 |       1791 |
|   5 |       710 |      4050 |      3232 |      2286 |      3292 |      2119 |      2312 |      1961 |       1897 |       2437 |
|   7 |      6808 |      1516 |      2402 |      3009 |      2641 |      3228 |      2672 |      2469 |       2374 |       1977 |
|   9 |      4247 |      4349 |      3200 |      1482 |      4832 |      3411 |      4011 |      2869 |       6195 |       5123 |
|  11 |      8159 |       740 |      4555 |      3814 |      4329 |      3639 |      4151 |      5008 |       2457 |       5188 |
|  13 |      6201 |      6560 |      3839 |      1972 |      6268 |      3979 |      4858 |      2094 |       6434 |       9104 |
|  15 |      1577 |      1886 |      1130 |      2666 |      5822 |      5392 |      6206 |      4662 |       6483 |       7993 |
|  17 |      1560 |      1554 |      1995 |      8542 |      8918 |      3124 |      3651 |      8594 |       5575 |       4182 |
|  19 |      1845 |     14482 |       950 |      6261 |     11848 |      7622 |      2552 |      9710 |       5844 |       7474 |
<!-- END_ADAM -->
<!-- START_CGD --> 
### CGD: Количество итераций ($\epsilon$=1e-05)
|   µ |   order=2 |   order=3 |   order=4 |   order=5 |   order=6 |   order=7 |   order=8 |   order=9 |   order=10 |   order=11 |
|----:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|----------:|-----------:|-----------:|
|   1 |         1 |         2 |         3 |         2 |         3 |         3 |         3 |         3 |          3 |          3 |
|   3 |         2 |         3 |         4 |         5 |         5 |         6 |         7 |         8 |          9 |          9 |
|   5 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |          9 |          9 |
|   7 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         8 |         10 |         11 |
|   9 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |          8 |         11 |
|  11 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |         10 |         11 |
|  13 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |         10 |         11 |
|  15 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |         10 |         11 |
|  17 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |         10 |         10 |
|  19 |         2 |         3 |         4 |         5 |         6 |         7 |         8 |         9 |          9 |         11 |
<!-- END_CGD -->