function [ A B ] = decomp_lu_crout(A,B)
    n = size(A,1);  %Numero de linhas de A

    %Calcula da matrix L -> armazenada em A
    for k = 1 : n
        for i = k : n
            sum = 0;
            for r = 1 : k-1
                printf("k %f i %f r %f\n", k, i, r)
                sum += A(i,r) * A(r,k);
            end
            A(i,k) = A(i,k) - sum;
        end


        # PRECISAMOS TROCAR AS LINHAS PARA CONTINUAR O PROCESSO QUANDO A DIAGONAL PRINCIPAL DE A OU DE L SÃO NULAS:
        # - SEM ZEROS NA DIAGONAL PRINCIPAL O PROCESSO DE DECOMPOSIÇÃO CONTINUA;
        # - VALORES DE DIAGONAIS MAIS ALTOS GERAM ARREDONDAMENTO MENORES;
        # - VAMOS ESCOLHER OS MAIORES VALORES DE CADA COLUNA DE L
        # Escolhe a melhor linha k

        [ A B ] = ftrocalinhasLUCrout (k,A,B);

    %Calcula da matrix U -> armazenada em A também, sobrepostas
        for j = k+1 : n
            sum = 0;
            for r = 1 : k-1
               sum += A(k,r) * A(r,j);
            end
            A(k,j) = ( A(k,j) - sum ) / A(k,k);
        end
    end

    %Matriz A armazena L e U, sobrepostos
end
