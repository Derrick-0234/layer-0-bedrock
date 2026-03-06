# Linear Regression Gradient (0.3)

Data: (x_i, y_i)
Model: y_hat_i = w*x_i + b
Loss: J(w,b) = (1/n) * sum_i (y_hat_i - y_i)^2

Let err_i = (w*x_i + b) - y_i

dJ/dw:
J = (1/n) * sum(err_i^2)
dJ/dw = (1/n) * sum(2*err_i * d(err_i)/dw)
d(err_i)/dw = x_i
=> dJ/dw = (2/n) * sum(err_i * x_i)

dJ/db:
d(err_i)/db = 1
=> dJ/db = (2/n) * sum(err_i)

Gradient descent updates:
w <- w - alpha * dJ/dw
b <- b - alpha * dJ/db
