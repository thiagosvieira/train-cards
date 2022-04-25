import {
    BrowserRouter as Router,
    Route,
    Routes,
    Navigate
  } from "react-router-dom";
import Exercicio from "./components/Exercicio";
import Home from "./pages/home/Home";
import Treinamentos from "./pages/treinamentos/Treinamentos";

export function AppRoutes(){
    return (
        <Router>
            <Routes>
                <Route path="/home" element={ <Home /> }></Route>
                <Route path="/treinamentos" element={ <Treinamentos /> }></Route>
                <Route path="/exercicio" element={ <Exercicio /> }></Route>
                <Route path="*" element={<Navigate to="/home" />} />
            </Routes>
        </Router>
    )
}