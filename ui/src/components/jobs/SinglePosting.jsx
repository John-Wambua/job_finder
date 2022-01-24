import {
    Avatar,
    Button, Card, CardActions, CardContent, CardHeader,
    Divider,
    Grid,
    Typography,
    colors
} from "@mui/material";


export default () =>{

    return (
        <Grid item >
            <Card sx={{ }} style={{marginBottom: '20px'}}>
                <CardHeader
                    avatar={
                        <Avatar sx={{ bgcolor: colors.red[500] }} aria-label="recipe">
                            S
                        </Avatar>
                    }

                    title="Microsoft"
                    subheader="Posted 30 days ago"
                />
                <CardContent>
                    <Typography gutterBottom variant="body1" component="div">
                        Software Engineer Intern
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        Lizards are a widespread group of squamate reptiles, with over 6,000
                        species, ranging across all continents except Antarctica
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small">View Job</Button>
                </CardActions>
            </Card>
            <Divider variant="inset" component="li" />
        </Grid>
    )
}