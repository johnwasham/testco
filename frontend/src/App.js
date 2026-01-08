import axios from "axios"
import logo from './logo.svg';
import './App.css';


function App() {

  axios
      .get("/api/customers/")
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err));

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hi there.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
