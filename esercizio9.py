anno=input("In che anno sei nato ")
if anno==1969:
    print("Sei nato nell' anno in cui l'uomo è stato sulla luna ")
if anno>1969:
    anno=anno-1969
    print("sei nato "+ str(anno)+ " anni dopo")
if anno<1969:
    anno=1969-anno
    print("sei nato "+ str(anno)+ " anni prima")

