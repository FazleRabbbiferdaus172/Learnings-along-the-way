const initialWagonState = {
    supplies: 100,
    distance: 0,
    days: 0
  };
  
  const gameReducer = (state=initialWagonState, action) => {
    switch (action.type) {
      case 'gather': {
        return {...state,
          supplies: state.supplies + 15,
          days: state.days + 1
        };
      }
      case 'travel': {
        const need = 20*action.payload;
        return need > state.supplies ? {...state} : {...state,
          supplies: state.supplies - 20*action.payload,
          distance: state.distance + 10,
          days: state.days + action.payload
        };
      }
  
    case 'tippedWagon': {
      return {
        ...state,
          supplies: state.supplies - 30,
          days: state.days + 1
      };
    }
  
      default: {
        return state;
      }
    }
  }
  
  let wagon = gameReducer(undefined, {});
  wagon = gameReducer(wagon, {type: 'travel', payload: 1});
  wagon = gameReducer(wagon, {type: 'gather', });
  wagon = gameReducer(wagon, {type: 'tippedWagon', });
  wagon = gameReducer(wagon, {type: 'travel', payload: 3});
  console.log(wagon)