import React from "react";

export default class CrearEncuesta extends React.Component {
  
  constructor(props) {
		super(props);
    this.handleChildren = this.handleChildren.bind(this);
    this.state = {
      questions: this.props.questions,
      //isFull: this.props.questions.length === 3 ? true: false, 
      isFull: false,
      len: 0
    };
      
	}

  handleChildren(e) {
    const handlePattern = this.props.handlePattern;
    const qs = this.state.questions;
    qs[parseInt(e.target.id[1])] = document.getElementById(`${e.target.id}`).value;
    this.setState({questions: qs});
    handlePattern(qs);
    
  }
  
  render() {
    const isFull = this.state.isFull;
    if (!isFull) {

      return (
        <div  id="container-question-1">
          <h2>Crear Encuesta</h2>
            
            <input type="text" id="q0" name="p1" value={this.state.questions[0]} onChange={this.handleChildren}/>
            <br/>
            <input type="text" id="q1" name="p2" value={this.state.questions[1]} onChange={this.handleChildren}/>
            <br/>
            <input type="text" id="q2" name="p3" value={this.state.questions[2]} onChange={this.handleChildren}/>
            <ul>
                {this.props.questions.map(function(question){
                    var key = Math.random().toString(36).substring(7);
                    return (
                      <>
                        <h4 key={ key }>Pregunta {question}</h4>
                        <br/>
                      </>
                    );
                  })}
          </ul>
      
          </div>
        );
    } else {
      return (
        <div id="container-question-2">
          <h2>Esta es la Encuesta</h2>
          <ul>
                {this.props.questions.map(function(question){
                    var key = Math.random().toString(36).substring(7);
                    return (
                      <>
                        <h4 key={ key }>{question}</h4>
                        <br/>
                      </>
                    );
                  })}
          </ul>
            
          </div>
        );
    }
  }
}