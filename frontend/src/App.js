import React, { createContext, useState } from 'react';
import CardContainer from './components/MoviesContainer';
import MovieDetail from './components/MovieDetail';
import Navbar from './components/Navbar';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import LogIn from './components/LogIn';
import SignUp from './components/SignUp';

export const UserLoggedInContext = createContext();

function App() {
  const [isUserLoogedIn, setIsUserLoogedIn] = useState(Boolean(localStorage.getItem('email')));

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
          <Route path='/login' element={ isUserLoogedIn ?  <Navigate to='/' /> : <LogIn /> } />
          <Route path='/signup' element={ isUserLoogedIn ?  <Navigate to='/' /> : <SignUp /> } />
        </Routes>
      </BrowserRouter>
    </UserLoggedInContext.Provider>

  );
}

export default App;
