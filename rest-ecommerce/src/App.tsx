import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navigation from "./components/Navigation/navigation";
import Home from "./components/Home/home";
import Login from "./components/Login/login";
import { Navbar } from "react-bootstrap";
import Logout from "./components/Logout/logout";

function App() {
  return (
    <>
      <Router>
        <Navbar>
          <Navigation />
        </Navbar>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="users/login" element={<Login />} />
          <Route path="users/logout" element={<Logout />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
