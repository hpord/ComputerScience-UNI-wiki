import React from 'react';
import './States.css';

/**
 * Define States, un componente React de la tarea #2. del LAB06 del curso CC3S2 
 * La Data del Modelo para esta vista  (Los nombres de los estados) esta disponible 
 * en  window.cc3s2models.statesModel().
 */
class States extends React.Component {
	constructor(props) {
		super(props);
		console.log('window.cc3s2models.statesModel()', window.cc3s2models.statesModel());
		this.state = {
			array: window.cc3s2models.statesModel(),
			inputValue: '',
			flag: true
		};
		this.handleChangeBound = (event) => this.handleChange(event);
	}
	handleChange(event) {
		this.setState({ inputValue: event.target.value });
		for (let i = 0; i < this.state.array.length; i++) {
			if (this.state.array[i].toUpperCase().includes(this.state.inputValue.toUpperCase())) {
				this.state.flag = true;
				break;
			} else {
				this.state.flag = false;
			}
		}
	}
	render() {
		return (
			<div className="cont">
				<div className="inCont">
					<input id="inId" type="text" onChange={this.handleChangeBound} placeholder="Busca tu estado..." />
				</div>
				<div className="country">
					{this.state.array.map(
						(el) => (el.toUpperCase().includes(this.state.inputValue.toUpperCase()) ? <div>{el}</div> : '')
					)}
					{!this.state.flag ? 'No se encontró nada!' : ' '}
				</div>
			</div>
		);
	}
}

export default States;
