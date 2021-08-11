import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

import CrearEncuesta from './components/CrearEncuesta.js';
import ResponderEncuesta from './components/ResponderEncuesta.js';
import Home from './components/Home.js';
import './App.css';

class App extends React.Component {
	state = { 
    questions: ['', '', ''], 
    answers: ['', '', ''] 
  };

  handlePatternQuestion = (q) => {
    this.setState({questions: q});
  }

  handlePatternAnswer = (ans) => {
    this.setState({answers: ans});
  }

	render() {
		return (
			<Router>
				<div id="container">
					<ul>
						<h1>Mis encuestas</h1>
						<li>
							<Link to="/Crear">Crear Encuesta</Link>
						</li>
						<li>
							<Link to="/Responder">Responder Encuesta</Link>
						</li>
					</ul>

					<hr />

					<Switch>
						<Route exact path="/">
							<Home />
						</Route>
						<Route path="/Crear">
							<CrearEncuesta handlePattern = {this.handlePatternQuestion} questions = {this.state.questions}/>
						</Route>
						<Route path="/Responder">
							<ResponderEncuesta handlePattern = {this.handlePatternAnswer} answers = {this.state.answers}  questions = {this.state.questions}/>
						</Route>
					</Switch>
				</div>
			</Router>
		);
	}
}

export default App;
