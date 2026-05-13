import { createFileRoute } from "@tanstack/react-router";
import { CodigoAguiaLanding } from "@/components/landing/CodigoAguiaLanding";

export const Route = createFileRoute("/")({
  component: CodigoAguiaLanding,
  head: () => ({
    meta: [
      { title: "O Código Águia — Mentalidade, Disciplina e Riqueza na Era Digital" },
      {
        name: "description",
        content:
          "Desenvolva a mentalidade, disciplina e visão estratégica para construir riqueza e liberdade na era digital. eBook premium para empreendedores.",
      },
      { property: "og:title", content: "O Código Águia — eBook Premium" },
      {
        property: "og:description",
        content: "Um sistema para construir liberdade e prosperidade na era digital.",
      },
      { property: "og:type", content: "website" },
    ],
  }),
});
