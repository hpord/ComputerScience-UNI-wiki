import React from 'react';
import './Example.css';

/*
  Ya que este componente muestra código  incluimos el formateador  https://prismjs.com/
  Lo invocamos etiquetando los bloques de código con with  la clase class="language-jsx"
*/
import Prism from 'prismjs';
import 'prismjs/components/prism-jsx.js';
import '../../node_modules/prismjs/themes/prism.css';

/* eslint-disable  react/jsx-one-expression-per-line */
/* eslint-disable  react/destructuring-assignment */
/* eslint no-plusplus: ["error", { "allowForLoopAfterthoughts": true }] */

// Los componentes React  son  subclases de React.Componment.
class Example extends React.Component {
  constructor(props) {
    super(props); // Se debe primero ejecutar el constructor de  React.Component 

    // Los Componentes tienen una propiedad especial denominada "state" 
    // que contiene el estado del componente. Podemos inicializarla aqui.
    // Leemos la data del modelo de ejemplo en la variable de estado 'name'
    this.state = {
      name: window.cc3s2models.exampleModel().name,
      motto: window.cc3s2models.exampleModel().motto,
      counter: 0,
      inputValue: '',
      buttonWasClicked: '',
    };

    // Los eventos de React se llaman directamente desde manejadores de eventos del DOM 
    // asi que no podemos llamar  directamente los  metodos de esta clase. Entonces
    // generamos una nueva funcion que maneja  el evento  simplemente llamando
    // el metodo que maneja el evento.
    this.handleChangeBound = event => this.handleChange(event);
    // Nota: Modismo común en codigo React es usar JavaScript bind() 
    // para hacer que el metodo cumpla con  pasar this al metodo:
    //      this.handleChange = this.handleChange.bind(this);
  }

  // Los componentess React tienen varias "funciones del ciclo de vida" 
  // https://reactjs.org/docs/react-component.html
  // que se usan para informar al componente sobre eventos interesantes.
  

  // componentDidMount - Se llama cuando un componente es activado
  componentDidMount() {
    // Para demostrar la actualización del estado  definimos una funcion
    // que incrementa el estado del contador e instruye al DOM 
    // para que lo llame cada 2 segundos.
    /* eslint-disable react/no-access-state-in-setstate */
    const counterIncrFunc = () => this.setState({
      counter: this.state.counter + 1,
    });
    this.timerID = setInterval(counterIncrFunc, 2 * 1000);

    // Lanzar el coloreado del codigo
    Prism.highlightAll();
  }

  // componentWillUnmount - Es llamado cuando el Componente esta siendo desactivado.
  componentWillUnmount() {
    // Necesitamos decirle al DOM que deje de llamarnos de otro modo React
    // se quejará cuando llamamos  setState en un componente desactivado.
    clearInterval(this.timerID);
  }

  // Metodo que se llama cuando se escribe en la caja del texto de entrada .
  handleChange(event) {
    this.setState({ motto: event.target.value });
  }

  // Metodo que se llama cuando el boton es presionado
  /* eslint-disable-next-line no-unused-vars */
  handleButtonClick(buttonName, event) {
    this.setState({ buttonWasClicked: buttonName });
  }

  /* eslint-disable-next-line class-methods-use-this */
  outOfBandJSX(option) {
    let optionJSX;
    const listItems = [];
    if (option) {
      optionJSX = <div>La opcion era Verdadera</div>;
    } else {
      optionJSX = <div>La opcion era Falsa</div>;
    }
    for (let i = 0; i < 3; i++) {
      listItems[i] = <li key={i}>  Item {i} de la Lista </li>;
    }
    const retVal = (
      <div>
        {optionJSX}
        <ul>{listItems}</ul>
      </div>
    );

    return retVal;
  }

  render() {
    return (
      <div className="container Example">
        <h1>cc3s2 Lab06  Ejemplo de  React.js </h1>

        <div id="example-output">
          <label htmlFor="inId">Campo de entrada: </label>
          <input
            in="inId"
            type="text"
            value={this.state.motto}
            onChange={this.handleChangeBound}
          />
        </div>


        <div id="wrap" className="motto-update">
          {/* Su componente  para mostrar y actualizar el lema de su tarea #1  irá aqui */}
          <div id="content">
            <p>{this.state.name}</p>
            <p>{this.state.motto}</p>
          </div>
          
        </div>

        <p>
          Esta vista es un ejemplo de un 
          &nbsp;
          <a href="https://reactjs.org/docs/react-component.html" target="_blank" rel="noopener noreferrer">
             Componente de React.js 
          </a>
          &nbsp;
          denominado <span className="cc3s2-code-name">Example</span>.
          Est&aacute; localizado en el archivo
          <code>components/example/Example.jsx</code>.
          Parece una clase de JavaScript denominada Example que tiene un metodo denominado &nbsp;
          <span className="cc3s2-code-name">render</span>, el cual parece estar 
          escrito en algo parecido al HTML.
        </p>
        <p>
          Realmente este componente est&aacute; escrito en un lenguaje llamado &nbsp;
          <a href="https://reactjs.org/docs/introducing-jsx.html" target="_blank" rel="noopener noreferrer">
            JSX
          </a>
          &nbsp; que se ejecuta como un pre - procesador del lenguaje JSX que es parecido al HTML, 
          para pasarlo a  JavaScript. El  JavaScript generado  esta limitado a  llamadas a la funcion  
           &nbsp;
          <a href="https://reactjs.org/docs/react-api.html#createelement" target="_blank" rel="noopener noreferrer">
            createElement
          </a>
          &nbsp; de React.js . Esto nos permite escribir c&oacute;digo parecido al
          HTML para  describir lo que el componente mostrar&aacute; en la p&aacute;gina.
        </p>
        <p>
          Aunque JSX  se parece al  HTML, no es HTML. Algunas de las diferencias son 
          necesarias debido a la incorporación  en el JavaScript.
          Por ejemplo, en vez de &nbsp; <code>class=</code> &nbsp; utilizamos &nbsp;
          <code>className=</code> &nbsp; (class es una  palabra reservada de JavsScript).
          Aunque es posible intercalar código JavaScript y JSX, se debe tener el cuidado
          necesario ya que el contenido de las etiquetas JSX se procesan como argumentos a una
          función, lo que limita lo que se puede hacer, como se verá a continuación.
        </p>

        <h3>Sustitución de Plantillas </h3>

        <p>
          JSX Trata el texto dentro de llaves (e.g. &nbsp; <code>{'{JavaScriptExpression}'}</code>)&nbsp; como
          plantillas donde la expresi&oacute;n de JavaScript es evaluada en el contexto de la  
          funcion actual y cuyo valor  reemplaza la plantilla en la cadena. La expresion puede 
          ser una cadena de  JavaScript o un valor recuperado de una expresion JSX. Esta caracerística 
          permite utilizar plantillas de HTML en la especificaci&oacute;n del componente.
        </p>

        <p>
          El constructor de la clase Example establece la propiedad  &nbsp; <code>state.name</code>  &nbsp; 
          (vea esta asignación de  &nbsp; <code>this.state.name</code>  &nbsp; en  &nbsp;  <code>Example.jsx</code>)
           del modelo en el DOM  que tiene un valor de  &nbsp; {this.state.name}  &nbsp;
           as&iacute;:
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
              `<p>Mi Nombre es: "{this.state.name}".</p>`
            }
          </code>
        </pre>
        <p>
          Deber&iacute;a verse :
        </p>
        <p className="cc3s2-example-output">
        Mi Nombre es: &ldquo; {this.state.name} &rdquo;.
        </p>

        <h3>
          Enlace unidireccional de JavaScript a HTML
        </h3>

        <p>

        React propaga automáticamente cualquier cambio en el estado de JavaScript al
           las Plantillas JSX. Por  ejemplo
          el siguiente código: &nbsp; <code> ({'{this.state.counter}'}) </code>
           &nbsp; muestra  la propiedad state.counter del componente Example.
           El componente establece un temporizador
           que incrementa el contador cada 2 segundos. El valor del contador
           se puede ver  aquí: {this.state.counter}.

        </p>

        <h3>Control de flujo</h3>
        <p>
          La mayoría de los motores de plantillas incluyen soporte para hacer
           renderizado e iteración. En JSX está integrado, y se transpila a
           JavaScript para que podamos usar construcciones de lenguaje JavaScript 
           para administrar el control de  flujo.
        </p>
        <p>
           Una forma de efectuar el control usando JavaScript es asignar fragmentos JSX
           a  variables  JavaScript y utilizar operadores de  control de flujo  de JavaScript 
           de forma normal. Por ejemplo, la siguiente función selecciona entre las
           posibles líneas de salida basandose en un argumento  y
           usa un bucle for para completar una matriz. Estas variables de JavaScript
           luego se pueden referenciar en el JSX devuelto por la función.
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
`function outOfBandJSX(option) {
  var optionJSX;
  if (option) {
    optionJSX = <div>La opcion era Verdadera </div>;
  } else {
    optionJSX  = <div>La opcion era Falsa</div>;
  }
  var listItems = [];
  for (var i = 0; i < 3; i++) {
    listItems[i] = <li key={i}>Item {i} de la  Lista </li>;
  }
  var retVal =
    <div>
      {optionJSX}
      <ul>
        {listItems}
      </ul>
    </div>;

  return retVal;
}`
            }
          </code>
        </pre>
        <p>
            Llamando esta funcion desde una plantilla.
            (Ej.  &nbsp; <code>{'{this.outOfBandJSX(true)}'}</code>)
            &nbsp; se expandir&iacute;a a:
        </p>
        <div className="cc3s2-example-output">{this.outOfBandJSX(true)}</div>
        <p>
             Otra forma de lograr esto es incrustar las operaciones dentro
             de Llaves. Aunque cualquier codigo JavaScript  puede aparecer dentro
             de llaves, debe devolver una cadena o expresión JSX para que funcione.
             Las operaciones de control de flujo de JavaScript como if, for y while 
             no devuelven valores, por lo que plantillas
             como  &nbsp; <code> {'{if (bool) ... else ...}'} </code>  &nbsp; no funcionan.
        </p>
        <p>
            El siguiente codigo genera la salida anterior y  utiliza el operador
            de JavaScript {'"?:"'} y el soporte de la programacion funcional 
            para retornar siempre un valor en la plantilla:
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
`<div>
  option ? <div>La opcion era Verdadera </div> : <div>La opcion era Falsa</div> }
  <ul>
    {[0,1,2].map((i) =>  <li key={i}>Item {i} de la Lista</li>)}
  </ul>
</div>`
            }
          </code>
        </pre>
        <p>
          Operaciones Booleanas tales como 
           {'"&&"'} tambien pueden ser usadas para controlar lo que se muestra.
          Por ejemplo, el siguiente codigo 
          har&aacute; que la sentencia  aparezca entre dos paragrafos cuando algunos
          caracteres se tipean en la siguiente caja de entrada .
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
`<div>
  <p> Un paragrafo aparecerá; entre este parágrafo </p>
  {
    this.state.inputValue && (
      <p>Este texto aparecer&aacute; cuando this.state.inputValue sea verdadero.
        this.state.inputValue === {this.state.inputValue}
      </p>
    )
  }
  <p>... y éste cuando algunos caracteres se tipeen en la caja de texto abajo.</p>
</div>
`
            }
          </code>
        </pre>
        <p>
          Genera la salida:
        </p>
        <div className="cc3s2-example-output">
          <p>
          Un paragrafo aparecerá; entre este parágrafo
          </p>
          {
            this.state.inputValue
            && (
              <p>
                Este texto aparecer&aacute; cuando this.state.inputValue sea verdadero.
                this.state.inputValue === {this.state.inputValue}
              </p>
            )
          }
          <p>
          ... y éste cuando algunos caracteres se tipeen en la caja de texto abajo.
          </p>
        </div>

        <h3>Usando manejadores de eventos como en el DOM para ingreso de datos</h3>
        <p>
          El ingreso de datos en  React se hace utilizando manejadores de eventos como en DOM. Por ejemplo, sentencias de JSX como:
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
`<label htmlFor="inId">Input Field: </label>
<input type="text" value={this.state.inputValue} onChange={this.handleChangeBound} />`
            }
          </code>
        </pre>
        <p>
          mostrará el texto de la propiedad inputValue del estado del componente  
           en la caja de entrada  (comienza vacia) y llama la funcion 
           this.handleChangedBound cada vez que el campo de entrada cambia.
          
          Generalmente esta clase de entrada estará asociada con
          un &nbsp; <a href="https://reactjs.org/docs/handling-events.html">Boton</a> &nbsp; o 
          dentro de un &nbsp; <a href="https://reactjs.org/docs/forms.html">Formulario</a> &nbsp; para permitir
          al usuario  mostrar cuando ha terminado de cambiar el campo de entrada.
          Note las diferencias con el HTML:&nbsp;
          <code>onchange=</code> &nbsp; se convierte en: &nbsp; <code>onChange=</code> &nbsp; y
          &nbsp;<code>for=</code>&nbsp;  se convierte en &nbsp; <code>htmlFor=</code>.
        </p>

        {
        /* eslint-disable jsx-a11y/label-has-associated-control */
        /* eslint-disable jsx-a11y/label-has-for */
        }
        <div className="cc3s2-example-output">
          <label htmlFor="inId">Campo de Entrada:
          </label>
          <input id="inId" type="text" value={this.state.inputValue} onChange={this.handleChangeBound} />
        </div>
        <p>

          La función handleChangeBound actualiza this.state.inputValue con el
           valor del elemento DOM por lo que su valor
           se puede acceder como &nbsp;<code> {'{this.state.inputValue}'} </code> &nbsp; que
           devuelve &nbsp; &ldquo; {this.state.inputValue} &rdquo;. Tenga en cuenta que no podemos directamente
           llamar a &nbsp; <code> this.handleChange </code> &nbsp; ya que es un método de  funcion de un objeto
           que no está disponible para el DOM. Para manejar esto creamos una nueva
           función &nbsp; <code> this.handleChangeBound </code> &nbsp; que puede llamar al método y usarlo aquí.
        </p>
        <p>
          Si queremos pasar argumentos a funciones manejadoras de eventos podemos usar
          definiciones de funciones flecha en linea de la siguiente manera:
        </p>
        <pre className="cc3s2-example-code">
          <code className="language-jsx">
            {
`<div className="cc3s2-example-output">
  <p>Test de los clicks en el boton.
    {
      this.state.buttonWasClicked &&
      <span>El ultimo boton presionado fue: {this.state.buttonWasClicked}</span>
    }
  </p>
  <button
    type="button"
    onClick={e => this.handleButtonClick("uno", e)}
  >
    Llamar a la funcion  handleButtonClick con el boton uno
  </button>
  <button
    type="button"
    onClick={e => this.handleButtonClick("dos", e)}
  >
    Llamar a la funcion  handleButtonClick con el boton dos
  </button>
</div>`
            }
          </code>
        </pre>
        <p>
          Cuando el boton sea presionado este llamará a la funcion flecha 
          la cual llamará el metodo &nbsp; <code>handleButtonClick</code>&nbsp; 
          con el argumento especificado.
          
        </p>
        <div className="cc3s2-example-output">
          <p>
          Test de los clicks en el boton. {
              this.state.buttonWasClicked
              && <span>El ultimo boton presionado fue:  {this.state.buttonWasClicked}</span>
            }
          </p>
          <button type="button" onClick={e => this.handleButtonClick('uno', e)}>
          Llamar a la funcion  handleButtonClick con el boton uno
          </button>
          <button type="button" onClick={e => this.handleButtonClick('dos', e)}>
          Llamar a la funcion  handleButtonClick con el boton dos
          </button>
        </div>
      </div>
    );
  }
}

export default Example;
