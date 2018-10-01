
% 4 sistemas com termos independentes diferentes B e mesma matriz A.

A = [0  1  2;
     2 -1 -1;
     1  0  1;]
n = size(A,1)  %Numero de linhas de A

B = [1,  0,  3,  1;
     2,  1,  5, -1;
     3,  2,  7,  5;]
ns = size(B,2) %Numero de colunas de B

% XdoOctave = A \ B(:, 1)

X = fsolucaoLUcrout(A,B)

A
B

for j = 1 : ns
    rmax(j) = fresiduomaximo(A,B(:,j), X(:,j));
end

rmax
