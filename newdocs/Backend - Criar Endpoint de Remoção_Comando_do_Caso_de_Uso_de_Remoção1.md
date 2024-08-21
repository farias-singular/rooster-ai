```csharp
namespace Project.Application.UseCases.Brands.DeleteBrand
{
    public class DeleteBrandCommand : ICommand
    {
        public string Id { get; }
        public string OrganizationId { get; }

        public DeleteBrandCommand(string id, string organizationId)
        {
            Id = id;
            OrganizationId = organizationId;
        }
    }
}
```