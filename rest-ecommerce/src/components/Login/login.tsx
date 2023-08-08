import { useState } from "react";

function Login() {
  const [user, setUser] = useState({
    username: "",
    password: "",
  });
  return (
    <form>
      <div className="form-group">
        <label htmlFor="usernameInput">username</label>
        <input
          className="form-control"
          type="text"
          id="usernameInput"
          placeholder="username"
        />
      </div>
      <div className="form-groupe">
        <label htmlFor="passwordInput">password</label>
        <input
          type="password"
          className="form-control"
          id="passwordInput"
          placeholder="password"
        />
      </div>
      <button type="submit" className="btn btn-primary">
        Submit
      </button>
    </form>
  );
}

export default Login;
