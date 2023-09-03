import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./component/Authentications/Login/Login";
import App from "./App";
import Signup from "./component/Authentications/Signup/Signup";
import Profile from "./component/Authentications/Profile/Profile";
import Logout from "./component/Authentications/Logout/Logout";
import { UserProvider } from "./context/userContext";

function Router() {
  return (
    <div>
      <UserProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<App />} />
            <Route path="/users/login" element={<Login />} />
            <Route path="/users/signup" element={<Signup />} />
            <Route path="/users/profile" element={<Profile />} />
            <Route path="/users/logout" element={<Logout />} />
          </Routes>
        </BrowserRouter>
      </UserProvider>
    </div>
  );
}

export default Router;
