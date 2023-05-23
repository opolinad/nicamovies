import React, { createContext, useState } from 'react';
import CardContainer from './components/MoviesContainer';
import MovieDetail from './components/MovieDetail';
import Navbar from './components/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import LogIn from './components/LogIn';
import SignUp from './components/SignUp';

export const UserLoggedInContext = createContext(null);

function App() {
  const [isUserLoogedIn, setIsUserLoogedIn] = useState(false);

  return (
    <UserLoggedInContext.Provider
      value={{
        isUserLoogedIn,
        setIsUserLoogedIn
      }}
    >
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path='/' element={ <CardContainer /> } />
          <Route path='/movie/:movieId' element={ <MovieDetail /> } />
          <Route path='/login' element={ <LogIn /> } />
          <Route path='/signup' element={ <SignUp /> } />
        </Routes>
      </BrowserRouter>
    </UserLoggedInContext.Provider>

  );
}

export default App;
