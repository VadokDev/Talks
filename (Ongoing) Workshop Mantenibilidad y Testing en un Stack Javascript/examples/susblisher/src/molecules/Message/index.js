import Button from '@mui/material/Button';
const Message = ({ content, onClickHandler }) => {
  return (
    <Button onClick={onClickHandler} variant='outlined'>
      {content}
    </Button>
  );
};

export default Message;
