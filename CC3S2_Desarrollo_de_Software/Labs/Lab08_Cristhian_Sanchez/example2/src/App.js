import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import QuoteAndAuthor from './QuoteAndAuthor';
import quotes from './QuotesDatabase';
import './App.css';

let styles = {
	margin: 'auto',
	width: '500px'
};
class App extends React.Component {
	constructor() {
		super();
		this.state = {
			quote: quotes[0].quote,
			author: quotes[0].author
		};
	}

	captionHandle = (idx) => {
		const generateQuote = quotes[idx];
		this.setState({
			quote: generateQuote.quote,
			author: generateQuote.author
		});
	};

	randomColor() {
		const color = `rgb(
      ${Math.floor(Math.random() * 155)},
      ${Math.floor(Math.random() * 155)},
      ${Math.floor(Math.random() * 155)})`;
		return color;
	}

	render() {
		return (
			<div id="container">
				<div style={styles}>
					<Carousel onChange={this.captionHandle}>
						<div>
							<img
								src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg"
								alt="Hong Kong"
							/>
						</div>
						<div>
							<img
								src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp"
								alt="Singapore"
							/>
						</div>
						<div>
							<img
								src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp"
								alt="Japan"
							/>
						</div>
						<div>
							<img
								src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp"
								alt="Las Vegas"
							/>
						</div>
					</Carousel>
				</div>
				<div>
					<QuoteAndAuthor displayColor={this.randomColor} {...this.state} />
				</div>
			</div>
		);
	}
}

export default App;
