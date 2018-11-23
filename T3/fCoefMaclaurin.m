function c = fCoefMaclaurin(n)
    sr2 = sqrt(2);

    c = [
        + 1 / sr2
        - (pi)/(4 * sr2)
        - (pi^2) / (32 * sr2)
        + (pi^3) / (384 * sr2)
        + (pi^4) / (6144 * sr2)
        - (pi^5) / (122880 * sr2)
        - (pi^6) / (2949120 * sr2)
        + (pi^7) / (82575360 * sr2)
        + (pi^8) / (2642411520 * sr2)
        - (pi^9) / (95126814720 * sr2)
        - (pi^10) / (3805072588800 * sr2)
    ](1:n+1);
end