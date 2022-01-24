import React from "react"
import Home from "./upload/DropResume";
import JobPostings from "./jobs/JobPostings";
import {Container} from "@mui/material";

const App = ()=>{
    return (
        <Container>
            <Home/>
            <JobPostings/>

        </Container>
    )
}

export default App