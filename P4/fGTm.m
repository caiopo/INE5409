function GTm=fGTm(m)
    soma=0;
    for k=1:m
        x = cos((2*k-1)*pi/(2*m)); %m 'nós' de Tchebyschev
        soma = soma + cos(x);
    end
    GTm=pi/m*soma;
end
