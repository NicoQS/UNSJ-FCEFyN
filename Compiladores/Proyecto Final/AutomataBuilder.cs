using System;
using System.Collections.Generic;
using System.Linq;

public static class AutomataBuilder
{
    private static AFD automataActual;
    private static TablaSimbolos tabla;
    private static bool tieneTransiciones = false;
    private static int contadorErrores = 0;
    public static string UltimoArchivoHTML { get; set; }
    
    public static void IniciarAutomata(string nombre)
    {
        automataActual = new AFD(nombre);
        tabla = new TablaSimbolos();
        tieneTransiciones = false;
        contadorErrores = 0;
        Console.WriteLine(string.Format("Iniciando construcción del autómata: {0}", nombre));
    }
    
    public static void AgregarSimbolo(string simbolo)
    {
        if (automataActual != null)
        {
            automataActual.AgregarSimbolo(simbolo);
        }
    }
    
    public static void AgregarEstado(string nombreEstado)
    {
        if (automataActual != null)
        {
            automataActual.AgregarEstado(nombreEstado);
        }
    }

    public static bool AgregarEstadoConValidacion(string nombreEstado)
    {
        if (automataActual != null && tabla != null)
        {
            if (tabla.EstadoExiste(nombreEstado))
            {
                contadorErrores++;
                return false; // Estado duplicado - NO lo agregamos
            }
            tabla.AgregarEstado(nombreEstado);
            automataActual.AgregarEstado(nombreEstado);
            return true;
        }
        return false;
    }

    public static bool ValidarEstadoExiste(string nombreEstado)
    {
        return tabla != null && tabla.EstadoExiste(nombreEstado);
    }

    public static bool ValidarEstadoFinal(string nombreEstado)
    {
        if (!ValidarEstadoExiste(nombreEstado))
        {
            contadorErrores++;
            return false; // Estado final no declarado - NO lo agregamos
        }
        return true;
    }

    public static bool ValidarEstadoTransicion(string nombreEstado)
    {
        if (!ValidarEstadoExiste(nombreEstado))
        {
            contadorErrores++;
            return false; // Estado en transición no declarado
        }
        return true;
    }

    public static int ObtenerNumeroErrores()
    {
        return contadorErrores;
    }
    
    public static void DefinirEstadoInicial(string nombreEstado)
    {
        if (automataActual != null)
        {
            if (tabla != null && !tabla.EstadoExiste(nombreEstado))
            {
                tabla.AgregarEstado(nombreEstado);
            }
            automataActual.DefinirEstadoInicial(nombreEstado);
        }
    }
    
    public static void MarcarEstadoFinal(string nombreEstado)
    {
        if (automataActual != null)
        {
            automataActual.MarcarEstadoFinal(nombreEstado);
        }
    }
    
    public static void AgregarTransicion(string origen, string destino, string simbolo)
    {
        if (automataActual != null)
        {
            automataActual.AgregarTransicion(origen, destino, simbolo);
        }
    }

    public static bool AgregarTransicionConValidacion(string origen, string destino, string simbolo)
    {
        if (automataActual != null && tabla != null)
        {
            string claveTransicion = origen + "-" + simbolo;
            if (tabla.TransicionExiste(claveTransicion))
            {
                contadorErrores++;
                return false; // Transicion duplicada - NO la agregamos
            }
            
            // Solo agregar si no hay errores de estados
            tabla.AgregarTransicion(claveTransicion, destino);
            tabla.AgregarSimbolo(simbolo);
            automataActual.AgregarTransicion(origen, destino, simbolo);
            tieneTransiciones = true;
            return true;
        }
        return false;
    }

    public static bool TieneTransiciones()
    {
        return tieneTransiciones;
    }

    public static bool ValidarAutomataCompleto()
    {
        if (automataActual == null || tabla == null)
        {
            return false;
        }

        // Verificar que hay al menos un estado
        if (tabla.NumeroEstados() == 0)
        {
            Console.WriteLine("ERROR: No se han definido estados.");
            return false;
        }

        // Verificar que hay estado inicial
        if (string.IsNullOrEmpty(automataActual.EstadoInicial))
        {
            Console.WriteLine("ERROR: No se ha definido estado inicial.");
            return false;
        }

        // Verificar que hay al menos una transición
        if (!tieneTransiciones)
        {
            Console.WriteLine("ERROR: No se han definido transiciones.");
            return false;
        }

        return true;
    }
    
    public static void FinalizarAutomata()
    {
        if (automataActual != null)
        {
            Console.WriteLine("\n" + new string('=', 60));
            Console.WriteLine("AUTÓMATA FINITO DETERMINISTA CONSTRUIDO EXITOSAMENTE");
            Console.WriteLine(new string('=', 60));
            
            // Mostrar tabla de símbolos
            if (tabla != null)
            {
                tabla.MostrarTablaSimbolos();
            }
            
            automataActual.MostrarInformacion();
            automataActual.GenerarVisualizacion();
            
            Console.WriteLine("\n" + new string('=', 60));
            Console.WriteLine("Se ha generado el archivo: " + UltimoArchivoHTML);
            Console.WriteLine("Ábrelo en tu navegador para ver el autómata gráficamente");
            Console.WriteLine(new string('=', 60));
        }
    }

    public static void FinalizarConValidacion()
    {
        if (automataActual != null && tabla != null)
        {
            Console.WriteLine("\n" + new string('=', 60));
            Console.WriteLine("RESUMEN DE VALIDACIÓN DEL AUTÓMATA");
            Console.WriteLine(new string('=', 60));
            
            if (contadorErrores > 0)
            {
                Console.WriteLine("\n❌ AUTÓMATA INVÁLIDO - Se encontraron {0} error(es)", contadorErrores);
                Console.WriteLine("NO se puede generar la visualización.");
                
                // Mostrar solo la tabla de símbolos con estados válidos
                tabla.MostrarTablaSimbolos();
            }
            else
            {
                // Mostrar tabla de símbolos
                tabla.MostrarTablaSimbolos();
                
                // Validar completitud
                bool valido = ValidarAutomataCompleto();
                
                if (valido)
                {
                    Console.WriteLine("\n✅ AUTÓMATA VÁLIDO - Generando visualización...");
                    automataActual.MostrarInformacion();
                    automataActual.GenerarVisualizacion();
                    
                    Console.WriteLine("\n" + new string('=', 60));
                    Console.WriteLine("Se ha generado el archivo: " + UltimoArchivoHTML);
                    Console.WriteLine("Ábrelo en tu navegador para ver el autómata gráficamente");
                    Console.WriteLine(new string('=', 60));
                }
                else
                {
                    Console.WriteLine("\n❌ AUTÓMATA INCOMPLETO - Faltan secciones obligatorias");
                    Console.WriteLine("NO se puede generar la visualización.");
                }
            }
        }
    }
    
    public static AFD ObtenerAutomata()
    {
        return automataActual;
    }
}

public class AFD
{
    public string Nombre { get; private set; }
    public HashSet<string> Estados { get; private set; }
    public HashSet<string> Alfabeto { get; private set; }
    public string EstadoInicial { get; private set; }
    public HashSet<string> EstadosFinales { get; private set; }
    public Dictionary<string, Dictionary<string, string>> Transiciones { get; private set; }
    
    public AFD(string nombre)
    {
        Nombre = nombre;
        Estados = new HashSet<string>();
        Alfabeto = new HashSet<string>();
        EstadosFinales = new HashSet<string>();
        Transiciones = new Dictionary<string, Dictionary<string, string>>();
        EstadoInicial = null;
    }
    
    public void AgregarSimbolo(string simbolo)
    {
        Alfabeto.Add(simbolo);
    }
    
    public void AgregarEstado(string estado)
    {
        if (!Estados.Contains(estado))
        {
            Estados.Add(estado);
            Console.WriteLine(string.Format("  Estado agregado: {0}", estado));
        }
    }
    
    public void DefinirEstadoInicial(string estado)
    {
        if (!Estados.Contains(estado))
        {
            AgregarEstado(estado);
        }
        EstadoInicial = estado;
        Console.WriteLine(string.Format("  Estado inicial definido: {0}", estado));
    }
    
    public void MarcarEstadoFinal(string estado)
    {
        if (Estados.Contains(estado))
        {
            EstadosFinales.Add(estado);
            Console.WriteLine(string.Format("  Estado final marcado: {0}", estado));
        }
    }
    
    public void AgregarTransicion(string origen, string destino, string simbolo)
    {
        // Asegurar que los estados existen
        if (!Estados.Contains(origen))
        {
            AgregarEstado(origen);
        }
        if (!Estados.Contains(destino))
        {
            AgregarEstado(destino);
        }
        
        // Agregar símbolo al alfabeto
        if (!Alfabeto.Contains(simbolo))
        {
            Alfabeto.Add(simbolo);
        }
        
        // Agregar transición
        if (!Transiciones.ContainsKey(origen))
        {
            Transiciones[origen] = new Dictionary<string, string>();
        }
        
        Transiciones[origen][simbolo] = destino;
        Console.WriteLine(string.Format("  Transición agregada: {0} --{1}--> {2}", origen, simbolo, destino));
    }
    
    public void MostrarInformacion()
    {
        Console.WriteLine(string.Format("\nNombre: {0}", Nombre));
        Console.WriteLine(string.Format("\nEstados: {{ {0} }}", string.Join(", ", Estados)));
        Console.WriteLine(string.Format("Alfabeto: {{ {0} }}", string.Join(", ", Alfabeto)));
        Console.WriteLine(string.Format("Estado Inicial: {0}", EstadoInicial));
        Console.WriteLine(string.Format("Estados Finales: {{ {0} }}", string.Join(", ", EstadosFinales)));
        
        Console.WriteLine("\nTabla de Transiciones:");
        Console.WriteLine("Estado\t| " + string.Join("\t| ", Alfabeto));
        Console.WriteLine(new string('-', 50));
        
        foreach (var estado in Estados.OrderBy(e => e))
        {
            Console.Write(estado + "\t| ");
            foreach (var simbolo in Alfabeto)
            {
                if (Transiciones.ContainsKey(estado) && Transiciones[estado].ContainsKey(simbolo))
                {
                    Console.Write(Transiciones[estado][simbolo] + "\t| ");
                }
                else
                {
                    Console.Write("-\t| ");
                }
            }
            Console.WriteLine();
        }
    }
    
    public void GenerarVisualizacion()
    {
        AutomataVisualizador.GenerarVisualizacion(this);
    }
}