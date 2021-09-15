import Category from "./component/Category";
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Login from "./component/Login";
import Customers from "./component/Customers";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/' component={Login} />
          <Route exact path='/category/' component={Category} />
          <Route exact path='/customers/' component={Customers} />
        </Switch>
      </Router>

    </div>
  );
}

export default App; 
