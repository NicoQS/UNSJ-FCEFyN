using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("╔═══════════════════════════════════════════════════════════════╗");
        Console.WriteLine("║  COMPILADOR DE AUTÓMATAS FINITOS DETERMINISTAS (AFD)         ║");
        Console.WriteLine("║  Versión 1.0 - Generado con Coco/R                           ║");
        Console.WriteLine("╚═══════════════════════════════════════════════════════════════╝\n");

        string archivoEntrada = null;

        if (args.Length > 0)
        {
            archivoEntrada = args[0];
        }
        else
        {
            Console.WriteLine("Uso: AutomataCompiler <archivo.aut>");
            Console.WriteLine("\nEjemplo de archivo de entrada (.aut):\n");
            MostrarEjemplo();
            Console.Write("\nIngrese la ruta del archivo de entrada: ");
            archivoEntrada = Console.ReadLine();
        }

        if (string.IsNullOrWhiteSpace(archivoEntrada))
        {
            Console.WriteLine("\n❌ Error: No se especificó archivo de entrada.");
            Console.WriteLine("\nPresione cualquier tecla para salir...");
            Console.ReadKey();
            return;
        }

        if (!File.Exists(archivoEntrada))
        {
            Console.WriteLine(string.Format("\n❌ Error: El archivo '{0}' no existe.", archivoEntrada));
            Console.WriteLine("\nPresione cualquier tecla para salir...");
            Console.ReadKey();
            return;
        }

        try
        {
            Console.WriteLine(string.Format("\n📂 Leyendo archivo: {0}", archivoEntrada));
            Console.WriteLine(new string('-', 60));

            Scanner scanner = new Scanner(archivoEntrada);
            Parser parser = new Parser(scanner);
            
            parser.Parse();

            if (parser.errors.count == 0)
            {
                Console.WriteLine("\n✅ Compilación exitosa - Sin errores");
            }
            else
            {
                Console.WriteLine(string.Format("\n❌ Compilación terminada con {0} error(es)", parser.errors.count));
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine(string.Format("\n❌ Error fatal: {0}", ex.Message));
            Console.WriteLine(ex.StackTrace);
        }

        Console.WriteLine("\n" + new string('=', 60));
        Console.WriteLine("Presione cualquier tecla para salir...");
        Console.ReadKey();
    }

    static void MostrarEjemplo()
    {
        Console.WriteLine(@"
════════════════════════════════════════════════════════════
AUTOMATA AutomataBinario

ESTADOS: q0, q1, q2

INICIAL: q0

FINALES: q2

TRANSICIONES:
    q0 -> q1 con ""0""
    q0 -> q0 con ""1""
    q1 -> q2 con ""0""
    q1 -> q0 con ""1""
    q2 -> q2 con ""0"", ""1""

FIN
════════════════════════════════════════════════════════════

Este ejemplo reconoce cadenas binarias que contienen al menos dos '0' consecutivos.
");
    }
}