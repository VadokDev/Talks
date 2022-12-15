import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';

const Read = ({ MessageMolecule, messages, readMessagesHandler }) => {
  return (
    <Grid alignContent={'center'}>
      <Box textAlign='center'>
        <Button
          variant='contained'
          onClick={readMessagesHandler}
          sx={{ mb: 2 }}
        >
          Leer Mensajes
        </Button>
      </Box>
      <Grid item>
        <Stack spacing={2}>
          {messages.map((message) => (
            <MessageMolecule content={message.content} />
          ))}
        </Stack>
      </Grid>
    </Grid>
  );
};

export default Read;
