import React, { useState, useEffect } from "react";
import { toast } from "react-toastify";
import { alpha, styled } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import Switch from "@mui/material/Switch";
import axios from "axios";

const Dashboard = () => {
  const [lightLoaded, setLightLoaded] = useState(false);
  const [soundLoaded, setSoundLoaded] = useState(false);
  const [airLoaded, setAirLoaded] = useState(false);

  const upData = async (type) => {
    try {
      const res = await axios.get(
        `http://localhost:3002/objetos/${type}/aumentar`
      );
      toast.success(res.data.message);
    } catch (err) {
      toast.error(err);
    }
  };
  const downData = async (type) => {
    try {
      const res = await axios.get(
        `http://localhost:3002/objetos/${type}/diminuir`
      );
      toast.success(res.data.message);
    } catch (err) {
      toast.error(err);
    }
  };

  const turnOnData = async (type) => {
    try {
      const res = await axios.get(
        `http://localhost:3002/objetos/${type}/ligar`
      );
      toast.success(res.data.message);
    } catch (err) {
      toast.error(err);
    }
  };

  const turnOffData = async (type) => {
    try {
      const res = await axios.get(
        `http://localhost:3002/objetos/${type}/desligar`
      );
      toast.success(res.data.message);
    } catch (err) {
      toast.error(err);
    }
  };

  // Som
  const [soundData, setSoundData] = useState([]);
  const getSound = async () => {
    try {
      const res = await axios.get("http://localhost:3002/objetos/caixaSom");
      setSoundData(res.data);
      setSoundLoaded(true);
    } catch (err) {
      toast.error(err);
    }
  };

  // Ar condicionado
  const [airData, setAirData] = useState([]);
  const getAir = async () => {
    try {
      const res = await axios.get(
        "http://localhost:3002/objetos/arcondicionado"
      );
      setAirData(res.data);
      setAirLoaded(true);
    } catch (err) {
      toast.error(err);
    }
  };

  // Lampada
  const [lightData, setLightData] = useState([]);
  const getLight = async () => {
    try {
      const res = await axios.get("http://localhost:3002/objetos/lampada");
      setLightData(res.data);
      setLightLoaded(true);
    } catch (err) {
      toast.error(err);
    }
  };

  useEffect(() => {
    const fetchData = () => {
      getLight();
      getSound();
      getAir();
    };

    fetchData(); // Chama a função inicialmente

    // Configura um intervalo para chamar a função a cada 5 segundos
    const intervalId = setInterval(fetchData, 5000);

    // Limpa o intervalo quando o componente é desmontado
    return () => clearInterval(intervalId);
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
  return airLoaded && soundLoaded && lightLoaded ? (
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
              {lightData.lampada.status ? "Ligado" : "Desligado"}
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">
              Sensor de Presença:
            </div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {lightData.sensor
                ? "Presença detectada"
                : "Presença não detectada"}
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={lightData.lampada.status}
            onClick={() => {
              if (!lightData.lampada.status) {
                turnOnData("lampada");
              } else {
                turnOffData("lampada");
              }
              getLight();
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
              {airData.sensor}°C
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Ar-condicionado:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {airData.Ar_condicionado.temperatura}°C
            </div>
            <div className="flex gap-1">
              <i
                className="fa-solid fa-plus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "
                onClick={() => {
                  upData("temperatura");
                  getAir();
                }}
              ></i>
              <i
                className="fa-solid fa-minus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "
                onClick={() => {
                  downData("temperatura");
                  getAir();
                }}
              ></i>
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Status:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {airData.Ar_condicionado.status ? "Ligado" : "Desligado"}
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={airData.Ar_condicionado.status}
            onClick={() => {
              if (!airData.Ar_condicionado.status) {
                turnOnData("arCond");
              } else {
                turnOffData("arCond");
              }
              getAir();
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
              {soundData.sensor}db
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Caixa de Som:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {soundData.Caixa_de_som.volume}%
            </div>
            <div className="flex gap-1">
              <i
                className="fa-solid fa-plus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "
                onClick={() => {
                  upData("som");
                  getSound();
                }}
              ></i>
              <i
                className="fa-solid fa-minus p-1 cursor-pointer rounded-full border text-red-800 border-red-800 bg-white hover:bg-red-800 hover:text-white duration-500 ease-in-out dark:bg-slate-800 dark:border-white dark:text-white dark:hover:bg-slate-700 "
                onClick={() => {
                  downData("som");
                  getSound();
                }}
              ></i>
            </div>
          </div>
          <div className="flex gap-3">
            <div className="text-slate-400 font-medium">Status:</div>
            <div className="text-md font-medium text-red-800 dark:text-white duration-500 ease-in-out">
              {soundData.Caixa_de_som.status ? "Ligado" : "Desligado"}
            </div>
          </div>
          <RedSwitch
            {...label}
            checked={soundData.Caixa_de_som.status}
            onClick={() => {
              if (!soundData.Caixa_de_som.status) {
                turnOnData("caixaSom");
              } else {
                turnOffData("caixaSom");
              }
              getSound();
            }}
          />
        </div>
      </div>
    </div>
  ) : null;
};

export default Dashboard;
