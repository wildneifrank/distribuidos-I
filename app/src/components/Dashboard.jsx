import React, { useState, useEffect } from "react";
import { toast } from "react-toastify";
import { alpha, styled } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import Switch from "@mui/material/Switch";
import axios from "axios";

const Dashboard = () => {
  const [light, setLight] = useState(false);
  const [sensor, setSensor] = useState(false);
  const [sound, setSound] = useState(false);

  const [data, setData] = useState([]);
  const getData = async () => {
    try {
      const res = await axios.get("http://localhost:3002/objeto");
      console.log(res.data);
      setData(res.data);
    } catch (err) {
      toast.error(err);
    }
  };
  useEffect(() => {
    getData();
  }, []);

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

      <div className="rounded-md bg-white shadow-lg h-auto lg:h-1/6 p-6 border-slate-100 border dark:bg-slate-800 duration-500 ease-in-out flex flex-col gap-2">
        <div className="w-full text-red-800 text-lg font-medium h-auto dark:text-white duration-500 ease-in-out">
          Lâmpada
        </div>
        <div className="w-full flex flex-col justify-center items-start">
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Status:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {light ? "Ligado" : "Desligado"}
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Sensor:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              Detectado
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={light}
            onClick={() => {
              setLight(!light);
              toast.success(
                `A lâmpada foi ${!light ? "ligada" : "desligada"} com sucesso!`
              );
            }}
          />
        </div>
      </div>
      <div className="rounded-md bg-white shadow-lg h-auto lg:h-1/6 p-6 border-slate-100 border dark:bg-slate-800 duration-500 ease-in-out flex flex-col gap-2">
        <div className="w-full text-red-800 text-lg font-medium h-auto dark:text-white duration-500 ease-in-out">
          Temperatura
        </div>
        <div className="w-full flex flex-col justify-center items-start">
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">
              Temperatura Ambiente:
            </div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              20°C
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Ar-condicionado:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              23°C
            </div>
            <div className="flex gap-1">
              <i className="fa-solid fa-plus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "></i>
              <i className="fa-solid fa-minus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "></i>
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Status:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {sensor ? "Ligado" : "Desligado"}
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={sensor}
            onClick={() => {
              setSensor(!sensor);
              toast.success(
                `o Ar-condicionado foi ${
                  !sensor ? "ligado" : "desligado"
                } com sucesso!`
              );
            }}
          />
        </div>
      </div>

      <div className="rounded-md bg-white shadow-lg h-auto lg:h-1/6 p-6 border-slate-100 border dark:bg-slate-800 duration-500 ease-in-out flex flex-col gap-2">
        <div className="w-full text-red-800 text-lg font-medium h-auto dark:text-white duration-500 ease-in-out">
          Som
        </div>
        <div className="w-full flex flex-col justify-center items-start">
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Som Ambiente:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              20db
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Caixa de Som:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              23db
            </div>
            <div className="flex gap-1">
              <i className="fa-solid fa-plus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "></i>
              <i className="fa-solid fa-minus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "></i>
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Status:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {sound ? "Ligado" : "Desligado"}
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={sound}
            onClick={() => {
              setSound(!sound);
              toast.success(
                `A Caixa de Som foi ${
                  !sound ? "ligada" : "desligada"
                } com sucesso!`
              );
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
