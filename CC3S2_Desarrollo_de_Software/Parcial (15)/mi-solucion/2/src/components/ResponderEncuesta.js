import React from "react";

export default class ResponderEncuesta extends React.Component {

  constructor(props) {
		super(props);
    this.handleChildren = this.handleChildren.bind(this);
    this.state = {
      answers: this.props.answers,
      questions: this.props.questions,
    };
      
	}

  handleChildren(e) {
    const handlePattern = this.props.handlePattern;
    const as = this.state.answers;
    as[parseInt(e.target.id[1])] = document.getElementById(`${e.target.id}`).value;
    this.setState({answers: as});
    handlePattern(as);
    
  }
  
  render() {

      return (
        <div id="container-answer-1">
          <h2>Esta es la encuesta</h2>
          <ul>
                {this.props.questions.map(function(q){
                    var key = Math.random().toString(36).substring(7);
                    return (
                      <>
                        <h4 key={ key }>Pregunta {q}</h4>
                        <br/>
                      </>
                    );
                  })}
          </ul>
          <br/>
          <h2>Responder encuesta</h2>
            
            <input type="text" id="a0" name="p1" value={this.state.answers[0]} onChange={this.handleChildren}/>
            <br/>
            <input type="text" id="a1" name="p2" value={this.state.answers[1]} onChange={this.handleChildren}/>
            <br/>
            <input type="text" id="a2" name="p3" value={this.state.answers[2]} onChange={this.handleChildren}/>
            <ul>
                {this.props.answers.map(function(answer){
                    var key = Math.random().toString(36).substring(7);
                    return (
                      <>
                        <h4 key={ key }>Respuesta a la pregunta {answer}</h4>
                        <br/>
                      </>
                    );
                  })}
          </ul>
      
          </div>
        );
    } 
};