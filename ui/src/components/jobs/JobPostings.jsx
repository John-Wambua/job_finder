import {Grid, List, Typography} from "@mui/material";
import SinglePosting from "./SinglePosting";


export default () =>{
    return (
        <Grid item>
            <Typography style={{fontWeight: '550'}} mt={2} variant="h5" gutterBottom component="div">
                Top Job Results
            </Typography>
            <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
                <SinglePosting/>
            </List>
        </Grid>

    )
}