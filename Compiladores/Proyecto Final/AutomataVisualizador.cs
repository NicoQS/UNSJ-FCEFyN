using System;
using System.Collections.Generic;
using System.Linq;

public static class AutomataVisualizador
{
    public static void GenerarVisualizacion(AFD automata)
    {
        // Crear la carpeta htmls_generados si no existe
        string carpetaSalida = "htmls_generados";
        if (!System.IO.Directory.Exists(carpetaSalida))
        {
            System.IO.Directory.CreateDirectory(carpetaSalida);
        }
        
        // Generar nombre del archivo con timestamp para evitar sobrescribir
        string timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
        string nombreArchivo = string.Format("{0}_{1}.html", automata.Nombre, timestamp);
        string rutaCompleta = System.IO.Path.Combine(carpetaSalida, nombreArchivo);
        
        var html = GenerarHTMLCompleto(automata);
        System.IO.File.WriteAllText(rutaCompleta, html);
        
        // Guardar la ruta del último archivo generado para mostrarla después
        AutomataBuilder.UltimoArchivoHTML = rutaCompleta;
    }
    
    private static string GenerarHTMLCompleto(AFD automata)
    {
        return string.Format(@"<!DOCTYPE html>
<html lang=""es"">
<head>
    <meta charset=""UTF-8"">
    <meta name=""viewport"" content=""width=device-width, initial-scale=1.0"">
    <title>Autómata: {0}</title>
    {1}
</head>
<body>
    <div class=""container"">
        <h1>🤖 Autómata Finito Determinista</h1>
        <div class=""subtitle"">Nombre: <strong>{0}</strong></div>
        
        {2}

        {3}

        <canvas id=""canvas"" width=""1000"" height=""600""></canvas>

        {4}

        {5}
    </div>

    {6}
</body>
</html>", 
            automata.Nombre,
            GenerarEstilosCSS(),
            GenerarSeccionInformacion(automata),
            GenerarControles(),
            GenerarLeyenda(),
            GenerarTablaTransiciones(automata),
            GenerarScriptJavaScript(automata));
    }
    
    private static string GenerarEstilosCSS()
    {
        return @"<style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            padding: 30px;
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .info-section {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .info-item {
            margin: 10px 0;
            font-size: 16px;
        }
        .label {
            font-weight: bold;
            color: #667eea;
        }
        #canvas {
            border: 2px solid #ddd;
            border-radius: 10px;
            display: block;
            margin: 20px auto;
            background: white;
            cursor: grab;
        }
        #canvas:active {
            cursor: grabbing;
        }
        .table-container {
            margin-top: 30px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }
        th {
            background-color: #667eea;
            color: white;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        tr:hover {
            background-color: #e9ecef;
        }
        .legend {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .legend-item {
            margin: 8px 0;
            display: flex;
            align-items: center;
        }
        .legend-icon {
            width: 40px;
            height: 40px;
            margin-right: 15px;
            border: 3px solid #333;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }
        .legend-icon.initial {
            border-color: #28a745;
            background: #d4edda;
        }
        .legend-icon.final {
            border: 5px double #dc3545;
            background: #f8d7da;
        }
        .controls {
            text-align: center;
            margin: 20px 0;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s;
        }
        button:hover {
            background: #5568d3;
        }
    </style>";
    }
    
    private static string GenerarSeccionInformacion(AFD automata)
    {
        return string.Format(@"<div class=""info-section"">
            <div class=""info-item"">
                <span class=""label"">Estados:</span> {{ {0} }}
            </div>
            <div class=""info-item"">
                <span class=""label"">Alfabeto:</span> {{ {1} }}
            </div>
            <div class=""info-item"">
                <span class=""label"">Estado Inicial:</span> {2}
            </div>
            <div class=""info-item"">
                <span class=""label"">Estados Finales:</span> {{ {3} }}
            </div>
        </div>",
            string.Join(", ", automata.Estados),
            string.Join(", ", automata.Alfabeto),
            automata.EstadoInicial,
            string.Join(", ", automata.EstadosFinales));
    }
    
    private static string GenerarControles()
    {
        return @"<div class=""controls"">
            <button onclick=""resetZoom()"">Restablecer Vista</button>
            <button onclick=""zoomIn()"">Acercar</button>
            <button onclick=""zoomOut()"">Alejar</button>
        </div>";
    }
    
    private static string GenerarLeyenda()
    {
        return @"<div class=""legend"">
            <h3>Leyenda:</h3>
            <div class=""legend-item"">
                <div class=""legend-icon initial"">q0</div>
                <span>Estado Inicial (círculo verde)</span>
            </div>
            <div class=""legend-item"">
                <div class=""legend-icon final"">qf</div>
                <span>Estado Final (doble círculo rojo)</span>
            </div>
            <div class=""legend-item"">
                <div class=""legend-icon"">q</div>
                <span>Estado Regular (círculo simple)</span>
            </div>
        </div>";
    }
    
    private static string GenerarTablaTransiciones(AFD automata)
    {
        var alfabetoOrdenado = automata.Alfabeto.OrderBy(s => s).ToList();
        var estadosOrdenados = automata.Estados.OrderBy(e => e).ToList();
        
        var tabla = @"
        <div class=""table-container"">
            <h3>Tabla de Transiciones</h3>
            <table>
                <thead>
                    <tr>
                        <th>Estado</th>";
        
        foreach (var simbolo in alfabetoOrdenado)
        {
            tabla += string.Format("<th>{0}</th>", simbolo);
        }
        
        tabla += @"
                    </tr>
                </thead>
                <tbody>";
        
        foreach (var estado in estadosOrdenados)
        {
            var marcador = "";
            if (estado == automata.EstadoInicial) marcador = "→ ";
            if (automata.EstadosFinales.Contains(estado)) marcador += "((";
            if (estado == automata.EstadoInicial || automata.EstadosFinales.Contains(estado))
                tabla += string.Format("<tr><td><strong>{0}{1}{2}</strong></td>", marcador, estado, (automata.EstadosFinales.Contains(estado) && marcador.Contains("((") ? "))" : ""));
            else
                tabla += string.Format("<tr><td>{0}</td>", estado);
            
            foreach (var simbolo in alfabetoOrdenado)
            {
                if (automata.Transiciones.ContainsKey(estado) && automata.Transiciones[estado].ContainsKey(simbolo))
                {
                    tabla += string.Format("<td>{0}</td>", automata.Transiciones[estado][simbolo]);
                }
                else
                {
                    tabla += "<td>-</td>";
                }
            }
            tabla += "</tr>";
        }
        
        tabla += @"
                </tbody>
            </table>
        </div>";
        
        return tabla;
    }
    
    private static string GenerarScriptJavaScript(AFD automata)
    {
        return string.Format(@"<script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        const estados = {0};
        const transiciones = {1};
        const estadoInicial = '{2}';
        const estadosFinales = new Set({3});

        let scale = 1;
        let offsetX = 0;
        let offsetY = 0;
        let isDragging = false;
        let lastX, lastY;

        function zoomIn() {{ scale *= 1.2; dibujar(); }}
        function zoomOut() {{ scale /= 1.2; dibujar(); }}
        function resetZoom() {{ scale = 1; offsetX = 0; offsetY = 0; dibujar(); }}

        {4}

        {5}

        {6}

        dibujar();
    </script>",
            GenerarEstadosJS(automata),
            GenerarTransicionesJS(automata),
            automata.EstadoInicial,
            GenerarEstadosFinalesJS(automata),
            GenerarEventosCanvas(),
            GenerarFuncionesDibujo(),
            GenerarFuncionesUtilidad());
    }
    
    private static string GenerarEstadosJS(AFD automata)
    {
        var estadosList = automata.Estados.ToList();
        var posiciones = new List<string>();
        int numEstados = estadosList.Count;
        double angleStep = 2 * Math.PI / numEstados;
        int radioCirculo = Math.Min(400, 150 + numEstados * 20);
        
        for (int i = 0; i < numEstados; i++)
        {
            double angle = i * angleStep - Math.PI / 2;
            int x = (int)(Math.Cos(angle) * radioCirculo);
            int y = (int)(Math.Sin(angle) * radioCirculo);
            posiciones.Add(string.Format("'{0}': {{x: {1}, y: {2}}}", estadosList[i], x, y));
        }
        
        return "{\n        " + string.Join(",\n        ", posiciones) + "\n    }";
    }
    
    private static string GenerarTransicionesJS(AFD automata)
    {
        var trans = new List<string>();
        foreach (var origen in automata.Transiciones.Keys)
        {
            foreach (var simbolo in automata.Transiciones[origen].Keys)
            {
                var destino = automata.Transiciones[origen][simbolo];
                trans.Add(string.Format("'{0}|{1}': '{2}'", origen, simbolo, destino));
            }
        }
        return "{\n        " + string.Join(",\n        ", trans) + "\n    }";
    }
    
    private static string GenerarEstadosFinalesJS(AFD automata)
    {
        return "[" + string.Join(", ", automata.EstadosFinales.Select(e => string.Format("'{0}'", e))) + "]";
    }
    
    private static string GenerarEventosCanvas()
    {
        return @"canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastX = e.offsetX;
            lastY = e.offsetY;
        });

        canvas.addEventListener('mousemove', (e) => {
            if (isDragging) {
                offsetX += (e.offsetX - lastX) / scale;
                offsetY += (e.offsetY - lastY) / scale;
                lastX = e.offsetX;
                lastY = e.offsetY;
                dibujar();
            }
        });

        canvas.addEventListener('mouseup', () => { isDragging = false; });
        canvas.addEventListener('mouseleave', () => { isDragging = false; });

        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            const zoom = e.deltaY < 0 ? 1.1 : 0.9;
            scale *= zoom;
            dibujar();
        });";
    }
    
    private static string GenerarFuncionesDibujo()
    {
        return @"function dibujar() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.save();
            ctx.translate(canvas.width / 2, canvas.height / 2);
            ctx.scale(scale, scale);
            ctx.translate(offsetX, offsetY);

            // Dibujar transiciones primero
            for (const [key, trans] of Object.entries(transiciones)) {
                const [origen, simbolo] = key.split('|');
                const destino = trans;
                const posOrigen = estados[origen];
                const posDestino = estados[destino];

                if (origen === destino) {
                    // Auto-transición (bucle)
                    dibujarAutoTransicion(posOrigen.x, posOrigen.y, simbolo);
                } else {
                    dibujarFlecha(posOrigen.x, posOrigen.y, posDestino.x, posDestino.y, simbolo);
                }
            }

            // Dibujar estados
            for (const [nombre, pos] of Object.entries(estados)) {
                const esInicial = nombre === estadoInicial;
                const esFinal = estadosFinales.has(nombre);
                dibujarEstado(pos.x, pos.y, nombre, esInicial, esFinal);
            }

            ctx.restore();
        }

        function dibujarEstado(x, y, nombre, esInicial, esFinal) {
            const radio = 35;
            
            // Flecha de entrada para estado inicial
            if (esInicial) {
                ctx.strokeStyle = '#28a745';
                ctx.fillStyle = '#28a745';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(x - 70, y);
                ctx.lineTo(x - radio - 5, y);
                ctx.stroke();
                // Punta de flecha
                ctx.beginPath();
                ctx.moveTo(x - radio - 5, y);
                ctx.lineTo(x - radio - 15, y - 5);
                ctx.lineTo(x - radio - 15, y + 5);
                ctx.closePath();
                ctx.fill();
            }

            // Círculo del estado
            ctx.strokeStyle = esInicial ? '#28a745' : esFinal ? '#dc3545' : '#333';
            ctx.fillStyle = esInicial ? '#d4edda' : esFinal ? '#f8d7da' : 'white';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(x, y, radio, 0, 2 * Math.PI);
            ctx.fill();
            ctx.stroke();

            // Círculo doble para estados finales
            if (esFinal) {
                ctx.beginPath();
                ctx.arc(x, y, radio - 7, 0, 2 * Math.PI);
                ctx.stroke();
            }

            // Nombre del estado
            ctx.fillStyle = '#000';
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(nombre, x, y);
        }

        function dibujarFlecha(x1, y1, x2, y2, etiqueta) {
            const radio = 35;
            const angulo = Math.atan2(y2 - y1, x2 - x1);
            const xOrigen = x1 + Math.cos(angulo) * radio;
            const yOrigen = y1 + Math.sin(angulo) * radio;
            const xDestino = x2 - Math.cos(angulo) * (radio + 5);
            const yDestino = y2 - Math.sin(angulo) * (radio + 5);

            // Línea
            ctx.strokeStyle = '#333';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(xOrigen, yOrigen);
            ctx.lineTo(xDestino, yDestino);
            ctx.stroke();

            // Punta de flecha
            const anguloFlecha = 0.3;
            const longitudFlecha = 15;
            ctx.fillStyle = '#333';
            ctx.beginPath();
            ctx.moveTo(xDestino, yDestino);
            ctx.lineTo(
                xDestino - longitudFlecha * Math.cos(angulo - anguloFlecha),
                yDestino - longitudFlecha * Math.sin(angulo - anguloFlecha)
            );
            ctx.lineTo(
                xDestino - longitudFlecha * Math.cos(angulo + anguloFlecha),
                yDestino - longitudFlecha * Math.sin(angulo + anguloFlecha)
            );
            ctx.closePath();
            ctx.fill();

            // Etiqueta
            const xMedio = (xOrigen + xDestino) / 2;
            const yMedio = (yOrigen + yDestino) / 2;
            ctx.fillStyle = 'white';
            ctx.fillRect(xMedio - 15, yMedio - 12, 30, 24);
            ctx.fillStyle = '#667eea';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(etiqueta, xMedio, yMedio);
        }

        function dibujarAutoTransicion(x, y, etiqueta) {
            const radio = 35;
            const radioLoop = 25;
            
            ctx.strokeStyle = '#333';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(x, y - radio - radioLoop, radioLoop, 0.3, Math.PI - 0.3);
            ctx.stroke();

            // Punta de flecha
            const anguloFlecha = Math.PI - 0.3;
            ctx.fillStyle = '#333';
            ctx.beginPath();
            ctx.moveTo(
                x + (radio + radioLoop) * Math.cos(anguloFlecha - 0.2),
                y - radio - radioLoop + (radio + radioLoop) * Math.sin(anguloFlecha - 0.2)
            );
            ctx.lineTo(
                x + (radio + radioLoop - 10) * Math.cos(anguloFlecha),
                y - radio - radioLoop + (radio + radioLoop) * Math.sin(anguloFlecha)
            );
            ctx.lineTo(
                x + (radio + radioLoop - 10) * Math.cos(anguloFlecha + 0.3),
                y - radio - radioLoop + (radio + radioLoop) * Math.sin(anguloFlecha + 0.3)
            );
            ctx.closePath();
            ctx.fill();

            // Etiqueta
            ctx.fillStyle = 'white';
            ctx.fillRect(x - 15, y - radio - radioLoop * 2 - 12, 30, 24);
            ctx.fillStyle = '#667eea';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(etiqueta, x, y - radio - radioLoop * 2);
        }";
    }
    
    private static string GenerarFuncionesUtilidad()
    {
        return "";
    }
}