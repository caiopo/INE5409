function rmax = fresiduomaximo(A,B,X)
    N = size(A,1);

    for i=1:N
        somatorio = sum(A(i, 1:N) .* transpose(X(1:N)));
        R(i) = abs(somatorio-B(i));
    end
    
    rmax = max(R);
end