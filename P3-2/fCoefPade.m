function [a b] = fCoefPade(n_pade, m_pade)
    c = fcoefMaclaurin(n_pade + m_pade);

%valido para n=n ou n=m+1
%calcular os bÂ´s via sistema de eqs.
    k = n_pade - m_pade;
    for i = 1 : m_pade
    	for j = 1 : i
    		A(i, j) = c(k + i + j);
    		A(j, i) = A(i, j);
    	end
    	B(i) = -c(n_pade + i + 1);
    end
    aux = A \ transpose(B);
    b = fliplr(transpose(aux)); %%b comeÃ§a de 1, igual no texto, e fliplr() inverte os indices do vetor
    b(m_pade + 1 : n_pade) = 0;
    b = [1 b]; %incluindo o 1Âº b, unitario
    a(1) = c(1);
    for i = 2 : n_pade + 1
    	S = c(i);
    	for j = 1 : i - 1
    		S = S + b(j + 1) * c(i - j);
    	end
    	a(i) = S;
    end
    b = b(1 : m_pade + 1);
end
