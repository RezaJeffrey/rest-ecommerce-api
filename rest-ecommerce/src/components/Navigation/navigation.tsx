import { useState, useEffect } from "react";

function Navigation() {
  const [isAuth, setIsAuth] = useState(false);
  useEffect(() => {
    if (localStorage.getItem("access_token") !== null) {
      setIsAuth(true);
    }
  }, [isAuth]);
  return (
    <ul className="nav nav-tabs">
      <li className="nav-item">
        <a className="nav-link" href="/">
          Home
        </a>
      </li>
      <li className="nav-item">
        {isAuth ? (
          <a className="nav-link" href="/users/logout">
            Logout
          </a>
        ) : (
          <a className="nav-link" href="/users/login">
            Login
          </a>
        )}
      </li>
    </ul>
  );
}

export default Navigation;
