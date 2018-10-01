function x = fnewton(f, xi, tol)
    while abs(dx) > tol && x < 100
        dx = -f(xi)/df(xi)
        x = xi + dx
        xi = x
    end
end