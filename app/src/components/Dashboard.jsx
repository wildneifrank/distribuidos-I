import React, { useState } from "react";
import { toast } from "react-toastify";
import { alpha, styled } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import Switch from "@mui/material/Switch";

const Dashboard = () => {
  const [light, setLight] = useState(false);
  const RedSwitch = styled(Switch)(({ theme }) => ({
    "& .MuiSwitch-switchBase.Mui-checked": {
      color: red[800],
      "&:hover": {
        backgroundColor: alpha(red[800], theme.palette.action.hoverOpacity),
      },
    },
    "& .MuiSwitch-switchBase.Mui-checked + .MuiSwitch-track": {
      backgroundColor: red[800],
    },
  }));

  const label = { inputProps: { "aria-label": "Switch demo" } };
  return (
    <div className="h-auto flex-1 flex flex-col gap-5 pl-20 pr-8 py-5 ">
      <div className="rounded-md bg-white dark:bg-slate-800 duration-500 ease-in-out shadow-lg py-3 justify-between h-auto sm:py-3 sm:h-1/6 flex items-center px-6 border-slate-100 border flex-wrap">
        <div className="w-full h-auto flex flex-col sm:w-2/3 lg:w-10/12">
          <div className="text-md text-slate-400 font-medium">Principal</div>
          <div className="text-xl text-red-800 font-semibold dark:text-white duration-500 ease-in-out">
            Dashboard
          </div>
        </div>
        <div className="flex-1 flex gap-3 items-center">
          <div className="text-lg text-red-800 font-medium dark:text-white duration-500 ease-in-out">
            Home Assistant
          </div>
          <img
            src="images/ufc.png"
            className="w-11 h-11 rounded-full border border-red-800 shadow-lg dark:border-white duration-500 ease-in-out"
            alt="Imagem do Admin"
          />
        </div>
      </div>
      <div className="rounded-md bg-white shadow-lg h-auto lg:h-1/6 p-6 border-slate-100 border dark:bg-slate-800 duration-500 ease-in-out">
        <div className="w-full text-red-800 text-lg font-medium h-auto dark:text-white duration-500 ease-in-out">
          Lâmpada
        </div>
        <div className="w-full flex gap-3 justify-start items-center">
          <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
            {light ? "Ligado" : "Desligado"}
          </div>
          <RedSwitch
            {...label}
            checked={light}
            className="duration-500 ease-in-out"
            onClick={() => {
              setLight(!light);
            }}
          />
        </div>
      </div>
      <div className="rounded-md bg-white shadow-lg py-3 justify-between h-auto sm:py-3 sm:h-auto flex items-center px-6 border-slate-100 border flex-wrap dark:bg-slate-800 duration-500 ease-in-out">
        <div className="w-full h-auto flex flex-col sm:w-2/3 lg:w-8/12">
          <div className="text-md text-slate-400 font-medium">lorem</div>
          <div className="text-xl text-red-800 font-semibold dark:text-white duration-500 ease-in-out">
            Lorem Ipsum
          </div>
          <input
            type="file"
            name="file"
            id="file"
            className="hidden"
            onChange={() => {
              toast.success("Arquivo upado com sucesso!");
            }}
          />
          <label
            htmlFor="file"
            className="px-4 py-2 lg:w-2/12 sm:w-3/12 text-center rounded-lg shadow-lg border border-red-800 text-red-800 tetx-lg font-semibold duration-500 ease-in-out hover:bg-red-800 hover:text-white cursor-pointer dark:text-white dark:bg-red-800 dark:hover:text-red-800 dark:hover:bg-white"
          >
            Anexar Arquivo
          </label>
        </div>
      </div>
      <div className="rounded-md bg-white text-red-800 dark:text-white font-medium shadow-lg h-auto px-6 py-4 flex flex-col gap-2 border-slate-100 border dark:bg-slate-800 duration-500 ease-in-out">
        <div className="w-full text-lg h-auto font-semibold">Lorem Ipsum</div>
        <div className="w-full h-auto border border-red-800 rounded-md shadow-md">
          <div className="w-full h-auto text-md flex gap-5 bg-red-800 text-white py-2 px-3">
            <div className="w-1/4 sm:w-2/6 flex items-center">Categoria</div>
            <div className="w-1/4 sm:w-2/6 flex items-center">
              Velocidade Média
            </div>
            <div className="w-1/4 sm:w-2/6 flex items-center">Placa</div>
            <div className="w-7 invisible">info</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
