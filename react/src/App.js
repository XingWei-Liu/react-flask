import logo from './logo.svg';
import './App.css';
import Clock from './Clock.js';
import ButtonEvent from './ButtonEvent.js';
import Loadpng from './Loadpng';

function App() {
  const tick = (
    <div className="App">
    <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <p>
        Edit <code>src/App.js</code> and save to reload.
      </p>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a>
      <Loadpng />
    </header>
  </div>
  );
  return tick;
}
//<Clock name='datetime'/>
export default App;