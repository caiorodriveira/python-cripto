// See https://aka.ms/new-console-template for more information
    Console.WriteLine("Tabuada");

Console.Write("Digite o valor: ");
Int value = Int.parse(Console.ReadLine());

for(int i=0;i<=10;i++){
    Console.WriteLine($"{value} X {i} = {value*i}");
}
