import React, { createContext, useState } from "react";

type userData = {
  username: string | null;
};

interface ContextProbs {
  user: userData | null;
  setUser: (user: userData) => void;
  isAuthenticated: () => boolean;
}

export const userContext = createContext<ContextProbs>({
  user: null,
  setUser: () => {},
  isAuthenticated: () => false,
});

export const UserProvider: React.FC<any> = ({ children }) => {
  const [user, setUser] = useState<userData | null>(null);
  const isAuthenticated = () => {
    return !!user;
  };
  return (
    <userContext.Provider value={{ user, setUser, isAuthenticated }}>
      {children}
    </userContext.Provider>
  );
};
